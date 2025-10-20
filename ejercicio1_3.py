
# en Codespaces: las figuras se guardan como PNG para abrir desde el panel de archivos.

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# --- Símbolos ---
x, y = sp.symbols('x y', real=True)

# pdf
f = sp.Rational(2,5) * (2*x + 3*y)

# 1) Normalización (integral en el cuadrado [0,1]x[0,1])
integral_total = sp.integrate(sp.integrate(f, (x, 0, 1)), (y, 0, 1))
print("Integral total (normalización) = ", sp.simplify(integral_total))  # debe ser 1

# 2) Probabilidad en R: 0 < x < y/2, 1/4 < y < 1/2
P_R = sp.integrate(sp.integrate(f, (x, 0, y/2)), (y, sp.Rational(1,4), sp.Rational(1,2)))
P_R_simpl = sp.simplify(P_R)
print("P((X,Y) in R) =", P_R_simpl, "≈", float(P_R_simpl))

# --- Mostrar pasos simbólicos (opcional) ---
# inner integral symbolic:
inner = sp.integrate(2*x + 3*y, (x, 0, y/2))
print("Inner integral (2x+3y) dx from 0 to y/2 =", sp.simplify(inner))
print("After multiplicative factor 2/5:", sp.simplify(sp.Rational(2,5)*inner))

# --- Gráficos ---
# 1) mapa de la densidad en el cuadrado [0,1]x[0,1]
nx, ny = 200, 200
xs = np.linspace(0, 1, nx)
ys = np.linspace(0, 1, ny)
X, Y = np.meshgrid(xs, ys)
F_vals = (2/5.0) * (2*X + 3*Y)

plt.figure(figsize=(9,4))

plt.subplot(1,2,1)
pcm = plt.pcolormesh(X, Y, F_vals, shading='auto')
plt.colorbar(pcm, label='f(x,y)')
plt.title('Mapa de densidad f(x,y) en [0,1]x[0,1]')
plt.xlabel('x'); plt.ylabel('y')

# 2) dibujo de la región R y sombreado
plt.subplot(1,2,2)
plt.pcolormesh(X, Y, F_vals, shading='auto', alpha=0.6)
# Region R: for y in [1/4, 1/2], x in [0, y/2]
ys_r = np.linspace(0.25, 0.5, 200)
xs_left = np.zeros_like(ys_r)
xs_right = ys_r / 2.0
plt.fill_betweenx(ys_r, xs_left, xs_right, color='yellow', alpha=0.8, label='Región R')
plt.xlim(0,1); plt.ylim(0,1)
plt.title('Región R sombreada (amarillo)')
plt.xlabel('x'); plt.ylabel('y')
plt.legend()

plt.tight_layout()
plt.savefig("pdf_and_region.png", dpi=150)
print("Gráfico guardado como pdf_and_region.png")
plt.show()
