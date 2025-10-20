from scipy.stats import norm

# Parámetros de la distribución
mu = 23      # media
sigma = 5    # desviación estándar
dias_mes = 30

# Probabilidad de que la temperatura esté entre 21 y 27
p = norm.cdf(27, mu, sigma) - norm.cdf(21, mu, sigma)

# Número esperado de días
dias_esperados = p * dias_mes

print(f"Probabilidad P(21 ≤ X ≤ 27) = {p:.4f}")
print(f"Número esperado de días = {dias_esperados:.2f}")
