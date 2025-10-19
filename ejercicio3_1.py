import math
import matplotlib.pyplot as plt

# --- Datos base ---
ingenieros = 5
abogados = 7

# --- Casos ---
# 1. Sin restricciones
formas1 = math.comb(ingenieros, 2) * math.comb(abogados, 3)

# 2. Un abogado determinado debe estar
formas2 = math.comb(ingenieros, 2) * math.comb(abogados - 1, 2)

# 3. Dos ingenieros determinados no pueden estar
formas3 = math.comb(ingenieros - 2, 2) * math.comb(abogados, 3)

# --- Mostrar resultados ---
print("===== FORMAS POSIBLES =====")
print(f"1️ Sin restricciones: {formas1:,}")
print(f"2️ Abogado determinado debe pertenecer: {formas2:,}")
print(f"3️ Ingenieros determinados NO pueden pertenecer: {formas3:,}")

# --- Visualización ---
eventos = [
    "Sin restricciones",
    "Abogado fijo",
    "Ingenieros excluidos"
]
valores = [formas1, formas2, formas3]

plt.figure(figsize=(8,5))
plt.bar(eventos, valores, color=['skyblue', 'lightgreen', 'salmon'])
plt.title("Número de formas posibles de formar el comité")
plt.ylabel("Número de combinaciones")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
