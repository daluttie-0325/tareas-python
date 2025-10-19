import math
import matplotlib.pyplot as plt
import networkx as nx

# --- Datos base ---
ingenieria = 4
ingles = 6
fisica = 2

# --- Cálculos combinatorios ---
# 1. Todos los libros de cada asignatura juntos
total_todos_juntos = math.factorial(3) * math.factorial(ingenieria) * math.factorial(ingles) * math.factorial(fisica)

# 2. Solo los de ingeniería juntos
total_solo_ing = math.factorial(9) * math.factorial(ingenieria)

# --- Mostrar resultados ---
print("===== RESULTADOS =====")
print(f"1️ Todos los libros de cada asignatura juntos: {total_todos_juntos:,} formas")
print(f"2️ Solo los libros de Ingeniería juntos: {total_solo_ing:,} formas")

# --- Visualización: gráfico de barras ---
eventos = ['Todos juntos', 'Solo Ingeniería juntos']
valores = [total_todos_juntos, total_solo_ing]

plt.figure(figsize=(8,5))
plt.bar(eventos, valores, color=['skyblue', 'lightcoral'])
plt.ylabel("Número de formas posibles")
plt.title("Ordenamiento de libros en un estante")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# --- Diagrama de árbol simple con NetworkX ---
G = nx.DiGraph()

# Nodos principales (asignaturas)
G.add_node("Inicio")
G.add_node("Ingeniería (4!)")
G.add_node("Inglés (6!)")
G.add_node("Física (2!)")

# Relaciones
G.add_edges_from([
    ("Inicio", "Ingeniería (4!)"),
    ("Inicio", "Inglés (6!)"),
    ("Inicio", "Física (2!)")
])

# Posiciones para el diagrama
pos = {
    "Inicio": (0, 0),
    "Ingeniería (4!)": (-1, -1),
    "Inglés (6!)": (0, -1),
    "Física (2!)": (1, -1)
}

plt.figure(figsize=(7,4))
nx.draw(G, pos, with_labels=True, node_color="lightyellow", node_size=2500, font_size=10, font_weight="bold", edge_color="gray")
plt.title("Diagrama de árbol: Bloques de libros por asignatura")
plt.show()
