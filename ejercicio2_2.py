import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Posibles sumas y sus frecuencias
x_vals = np.arange(2, 13)
freq = np.array([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1])
p_x = freq / 36  # Probabilidades

# Función de probabilidad acumulada
F_x = np.cumsum(p_x)

# Valor medio y varianza
E_X = np.sum(x_vals * p_x)
E_X2 = np.sum((x_vals ** 2) * p_x)
Var_X = E_X2 - E_X**2

# Tabla resumen
tabla = pd.DataFrame({
    "x": x_vals,
    "P(X=x)": p_x,
    "F(X≤x)": F_x
})

print(tabla)
print("\nValor medio (E[X]) =", round(E_X, 4))
print("Varianza (Var[X]) =", round(Var_X, 4))

# --- Gráficos ---
plt.figure(figsize=(10,4))

# Función de probabilidad
plt.subplot(1,2,1)
plt.stem(x_vals, p_x, basefmt=" ", use_line_collection=True)
plt.title("Función de probabilidad P(X=x)")
plt.xlabel("Suma de los dos dados")
plt.ylabel("Probabilidad")
plt.grid(True)

# Función de distribución acumulada
plt.subplot(1,2,2)
plt.step(x_vals, F_x, where="mid", color='orange')
plt.title("Función de distribución acumulada F(X≤x)")
plt.xlabel("Suma de los dos dados")
plt.ylabel("Probabilidad acumulada")
plt.grid(True)

plt.tight_layout()
plt.show()
