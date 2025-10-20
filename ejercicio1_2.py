import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Definimos la variable simbólica
x = sp.Symbol('x', real=True, nonnegative=True)
k = sp.Symbol('k', real=True, positive=True)

# Función de densidad
f = k * x**2

# 1️ Calcular k usando la condición de probabilidad total = 1
ecuacion = sp.Eq(sp.integrate(f, (x, 0, 6)), 1)
k_val = sp.solve(ecuacion, k)[0]

print(f"Constante de normalización k = {float(k_val):.5f}")

# Sustituir k en la función
f_x = f.subs(k, k_val)

# 2️ Función de distribución acumulada (CDF)
F_x = sp.integrate(f_x, (x, 0, x))
F_x_simplificada = sp.simplify(F_x)

print("\nFunción de distribución acumulada F(x):")
sp.pprint(F_x_simplificada)

# 3️ Valor medio y varianza
E_X = sp.integrate(x * f_x, (x, 0, 6))
E_X2 = sp.integrate(x**2 * f_x, (x, 0, 6))
Var_X = E_X2 - E_X**2

print(f"\nValor medio E[X] = {float(E_X):.4f}")
print(f"Varianza Var[X] = {float(Var_X):.4f}")

# 4️ Gráficos
x_vals = np.linspace(0, 6, 300)
f_vals = [f_x.subs(x, val) for val in x_vals]
F_vals = [F_x_simplificada.subs(x, val) for val in x_vals]

plt.figure(figsize=(10,5))

# Densidad de probabilidad
plt.subplot(1,2,1)
plt.plot(x_vals, f_vals, color='blue')
plt.title('Función de Densidad de Probabilidad')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)

# Función de distribución acumulada
plt.subplot(1,2,2)
plt.plot(x_vals, F_vals, color='green')
plt.title('Función de Distribución Acumulada (CDF)')
plt.xlabel('x')
plt.ylabel('F(x)')
plt.grid(True)

plt.tight_layout()
plt.show()
