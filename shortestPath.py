import matplotlib.pyplot as plt
import networkx as nx

# Crear el grafo
G = nx.Graph()

# Añadir los nodos y las aristas con sus respectivas distancias
edges = [
    ("Cádiz", "Puerto Real", 25),
    ("Cádiz", "San Fernando", 16),
    ("Puerto Real", "San Fernando", 12),
    ("Puerto Real", "Chiclana", 30),
    ("San Fernando", "Chiclana", 10),
    #("Cádiz", "Jerez de la Frontera", 35),
    ("Puerto Real", "Jerez de la Frontera", 22),
    ("San Fernando", "Jerez de la Frontera", 38),
    ("Chiclana", "Jerez de la Frontera", 40),
    ("Cádiz", "El Puerto de Santa María", 20),
    ("Puerto Real", "El Puerto de Santa María", 15),
    ("San Fernando", "El Puerto de Santa María", 25),
    ("Chiclana", "El Puerto de Santa María", 35),
    ("Cádiz", "Rota", 45),
    ("Puerto Real", "Rota", 40),
    ("San Fernando", "Rota", 50),
    ("Chiclana", "Rota", 55),
    ("Jerez de la Frontera", "Rota", 30),
    ("El Puerto de Santa María", "Rota", 20),
    ("Cádiz", "Arcos de la Frontera", 60),
    ("Puerto Real", "Arcos de la Frontera", 55),
    ("San Fernando", "Arcos de la Frontera", 65),
    ("Chiclana", "Arcos de la Frontera", 70),
    ("Jerez de la Frontera", "Arcos de la Frontera", 35),
    ("El Puerto de Santa María", "Arcos de la Frontera", 45)
]

# Añadir las aristas al grafo
G.add_weighted_edges_from(edges)

# Definir la posición de los nodos para visualización
pos = nx.spring_layout(G)  # Distribución automática de los nodos

# Dibujar el grafo
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='skyblue', font_size=10, font_weight='bold', edge_color='purple')

# Dibujar las etiquetas de las aristas (distancias)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Calcular la longitud del camino mínimo entre Cádiz y Chiclana
shortest_path_length = nx.shortest_path_length(G, source="Cádiz", target="Jerez de la Frontera", weight='weight')
shortest_path = nx.shortest_path(G, source="Cádiz", target="Jerez de la Frontera", weight='weight')

print("La distancia mas corta es de", shortest_path_length, "km") #Distancia mas corta
print("La ruta mas corta es", shortest_path)  #Camino mas corto

# Mostrar el gráfico
plt.title("Grafo de Ciudades y Distancias en la Bahía de Cádiz")
plt.show()