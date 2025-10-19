import math
import matplotlib.pyplot as plt

# --- 1️⃣ No obtener 7 u 11 en ninguno de los dos lanzamientos ---
p_no7_11_una = 28 / 36
p_no7_11_dos = (28 / 36) ** 2

# --- 2️⃣ Obtener tres 6 en 5 lanzamientos ---
n = 5
k = 3
p = 1/6
q = 1 - p

p_3_de_5 = math.comb(n, k) * (p**k) * (q**(n-k))

# --- Mostrar resultados ---
print("===== RESULTADOS =====")
print(f"1️ P(no obtener 7 u 11 en 2 lanzamientos) = {p_no7_11_dos:.5f}")
print(f"2️ P(obtener tres 6 en 5 lanzamientos) = {p_3_de_5:.5f}")

# --- Gráfico de resultados ---
eventos = ['No 7 u 11 (2 lanzamientos)', '3 veces el 6 (en 5 lanzamientos)']
valores = [p_no7_11_dos, p_3_de_5]

plt.figure(figsize=(8,5))
plt.bar(eventos, valores, color=['skyblue', 'lightcoral'])
plt.title("Probabilidades de eventos con dados")
plt.ylabel("Probabilidad")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
