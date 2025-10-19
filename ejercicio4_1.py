import math
import matplotlib.pyplot as plt

# --- Datos ---
total = 10          # total de estudiantes
electr = 5
sist = 2
indus = 3

# --- Cálculo de permutaciones con repetición ---
formas = math.factorial(total) // (math.factorial(electr) * math.factorial(sist) * math.factorial(indus))

print("===== RESULTADO =====")
print(f"Número total de formas distintas de ordenarlos: {formas:,}")

# --- Visualización simple (proporción por grupo) ---
labels = ['Electrónica (5)', 'Sistemas (2)', 'Industrial (3)']
sizes = [electr, sist, indus]
colors = ['skyblue', 'lightgreen', 'lightcoral']

plt.figure(figsize=(6,6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title("Distribución de estudiantes por carrera")
plt.show()

# --- Gráfico del resultado numérico ---
plt.figure(figsize=(5,4))
plt.bar(['Formas posibles'], [formas], color='gold')
plt.title("Número total de formas de ordenamiento (indistinguibles)")
plt.ylabel("Cantidad")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()
