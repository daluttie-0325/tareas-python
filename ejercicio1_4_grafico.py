import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(10, 40, 400)
y = norm.pdf(x, mu, sigma)

plt.plot(x, y, label='Distribución Normal (μ=23, σ=5)')
plt.fill_between(x, y, where=(x >= 21) & (x <= 27), color='skyblue', alpha=0.5, label='21°C ≤ X ≤ 27°C')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Densidad de probabilidad')
plt.legend()
plt.title('Distribución de temperaturas máximas en junio')
plt.show()
