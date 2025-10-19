import math
import matplotlib.pyplot as plt
import numpy as np

# Datos base
E = 8   # Electrónica
S = 3   # Sistemas
I = 9   # Industrial
N = E + S + I  # Total
r = 3   # Selecciones

# ---- FUNCIONES DE APOYO ----
def comb(n, k):
    return math.comb(n, k)

def prob_sin_reemplazo(exitos, total_exitos, total, seleccionados):
    """Probabilidad usando combinaciones sin reemplazo"""
    return comb(total_exitos, exitos) * comb(total - total_exitos, seleccionados - exitos) / comb(total, seleccionados)

# ---- PROBABILIDADES SIN REEMPLAZO ----
p_electro3 = comb(E, 3) / comb(N, 3)
p_sistemas3 = comb(S, 3) / comb(N, 3)
p_2E_1S = (comb(E, 2) * comb(S, 1)) / comb(N, 3)
p_almenos1S = 1 - (comb(N - S, 3) / comb(N, 3))
p_1E_1S_1I = (comb(E, 1) * comb(S, 1) * comb(I, 1)) / comb(N, 3)
p_orden_E_S_I = (E/N) * (S/(N-1)) * (I/(N-2))

# ---- PROBABILIDADES CON REEMPLAZO ----
# Con reemplazo (cada selección se hace con el mismo total N)
p_electro3_r = (E/N)**3
p_sistemas3_r = (S/N)**3
p_2E_1S_r = (math.comb(3, 2) * (E/N)**2 * (S/N))
p_almenos1S_r = 1 - ((1 - (S/N))**3)
p_1E_1S_1I_r = math.factorial(3)/(math.factorial(1)*math.factorial(1)*math.factorial(1)) * (E/N)*(S/N)*(I/N)
p_orden_E_S_I_r = (E/N)*(S/N)*(I/N)

# ---- MOSTRAR RESULTADOS NUMÉRICOS ----
eventos = [
    "3 Electrónica",
    "3 Sistemas",
    "2 Electrónica, 1 Sistemas",
    "≥1 Sistemas",
    "1 de cada carrera",
    "Orden E-S-I"
]

prob_sin = [
    p_electro3,
    p_sistemas3,
    p_2E_1S,
    p_almenos1S,
    p_1E_1S_1I,
    p_orden_E_S_I
]

prob_con = [
    p_electro3_r,
    p_sistemas3_r,
    p_2E_1S_r,
    p_almenos1S_r,
    p_1E_1S_1I_r,
    p_orden_E_S_I_r
]

print("===== Probabilidades SIN reemplazo =====")
for ev, p in zip(eventos, prob_sin):
    print(f"{ev}: {p:.6f}")

print("\n===== Probabilidades CON reemplazo =====")
for ev, p in zip(eventos, prob_con):
    print(f"{ev}: {p:.6f}")

# ---- GRÁFICO COMPARATIVO ----
x = np.arange(len(eventos))
width = 0.35

plt.figure(figsize=(10,6))
plt.bar(x - width/2, prob_sin, width, label='Sin reemplazo', color='skyblue')
plt.bar(x + width/2, prob_con, width, label='Con reemplazo', color='lightcoral')
plt.xticks(x, eventos, rotation=30)
plt.ylabel("Probabilidad")
plt.title("Probabilidades de selección de estudiantes por carrera")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

