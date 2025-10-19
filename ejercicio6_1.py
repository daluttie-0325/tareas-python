import math
import matplotlib.pyplot as plt
from scipy.stats import binom, poisson, norm

# --- Datos ---
n = 600       # memorias seleccionadas
p = 0.03      # probabilidad de defecto
x = 12

# --- 1️ Binomial exacta ---
p_binom = binom.pmf(x, n, p)

# --- 2️ Poisson aproximada ---
lambd = n * p
p_poisson = poisson.pmf(x, lambd)

# --- 3️ Normal aproximada ---
mu = n * p
sigma = math.sqrt(n * p * (1 - p))
z1 = (x - 0.5 - mu) / sigma
z2 = (x + 0.5 - mu) / sigma
p_normal = norm.cdf(z2) - norm.cdf(z1)

# --- Mostrar resultados ---
print("===== PROBABILIDAD DE 12 DEFECTUOSAS =====")
print(f"1️ Binomial exacta:  {p_binom:.6f}")
print(f"2️ Poisson aprox.:   {p_poisson:.6f}")
print(f"3️ Normal aprox.:    {p_normal:.6f}")

# --- Gráfico comparativo ---
etiquetas = ['Binomial', 'Poisson', 'Normal']
valores = [p_binom, p_poisson, p_normal]

plt.figure(figsize=(8,5))
plt.bar(etiquetas, valores, color=['skyblue','lightcoral','lightgreen'])
plt.title("Probabilidad de obtener 12 memorias defectuosas (n=600, p=0.03)")
plt.ylabel("Probabilidad")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
