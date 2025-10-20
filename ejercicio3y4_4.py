# ---------------------------------------------------------------
# Probabilidad de defectos en televisores SAMSUNG
# n = 85, p = 0.02, X = 4, lambda = 1.7
# ---------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, poisson

# Parámetros
n = 85       # número de televisores
p = 0.02     # probabilidad de defecto
x = 4        # número de defectuosos
lmbda = n * p  # valor esperado (λ = 1.7)

# --- 1. Usando distribución binomial ---
prob_binomial = binom.pmf(x, n, p)

# --- 2. Usando aproximación Poisson ---
prob_poisson = poisson.pmf(x, lmbda)

print(f"Probabilidad exacta (Binomial): {prob_binomial:.6f}")
print(f"Aproximación Poisson: {prob_poisson:.6f}")

# --- 3. Gráfica de ambas distribuciones ---
x_vals = np.arange(0, 10)
binom_vals = binom.pmf(x_vals, n, p)
poiss_vals = poisson.pmf(x_vals, lmbda)

plt.figure(figsize=(8, 5))
plt.bar(x_vals - 0.2, binom_vals, width=0.4, label="Binomial", alpha=0.7)
plt.bar(x_vals + 0.2, poiss_vals, width=0.4, label="Poisson", alpha=0.7)
plt.title("Distribución de defectos en televisores SAMSUNG")
plt.xlabel("Número de televisores defectuosos (X)")
plt.ylabel("Probabilidad P(X = x)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()
