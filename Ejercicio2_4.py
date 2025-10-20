import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

# Parámetros
media = 5000
lambd = 1 / media

# Cálculo del valor solicitado
p = 0.9
x0 = -np.log(p) / lambd
print(f"Duración informada: {x0:.2f} horas")

# Graficar distribución exponencial
x = np.linspace(0, 25000, 1000)
y = expon.pdf(x, scale=1/lambd)

plt.figure(figsize=(8, 5))
plt.plot(x, y, label='Distribución Exponencial (media=5000)')
plt.fill_between(x, 0, y, where=(x > x0), color='skyblue', alpha=0.5, label='Área: P(X > x₀) = 0.9')
plt.axvline(x0, color='red', linestyle='--', label=f'x₀ = {x0:.0f} h')
plt.title('Duración de baterías (Distribución Exponencial)')
plt.xlabel('Duración (horas)')
plt.ylabel('Densidad de probabilidad')
plt.legend()
plt.grid(True)
plt.show()
