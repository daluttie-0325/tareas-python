import math
import itertools
import pandas as pd

# Total de estudiantes
n_sistemas = 3
n_electronica = 2
n_industrial = 3
total = n_sistemas + n_electronica + n_industrial

# Total de combinaciones posibles
N = math.comb(total, 2)

# Posibles valores de (x, y)
valores = [(x, y) for x in range(3) for y in range(3) if x + y <= 2]

# Calcular f(x,y)
def f(x, y):
    return math.comb(n_sistemas, x) * math.comb(n_electronica, y) * math.comb(n_industrial, 2 - x - y) / N

# Crear tabla de resultados
datos = [(x, y, f(x, y)) for x, y in valores]
tabla = pd.DataFrame(datos, columns=["x (Sistemas)", "y (Electrónica)", "f(x,y)"])

# Probabilidad de R = {(x,y) | x + y <= 1}
p_R = sum(f(x, y) for x, y in valores if x + y <= 1)

print("Función de probabilidad conjunta f(x,y):")
print(tabla)
print(f"\nProbabilidad P(R) = {p_R:.4f}")
