import networkx as nx
import matplotlib.pyplot as plt
import osmnx as ox

edges = [('A', 'B', 640),
         ('A', 'C', 200),
         ('A', 'E', 170),
         ('A', 'G', 205),
         ('B', 'E', 130),
         ('B', 'F', 185),
         ("C", "D", 100),
         ('C', 'E', 140),
         ('C', 'H', 100),
         ('C', 'G', 190),
         ('D', 'H', 180),
         ('D', 'G', 115),
         ("D", "K", 665),
         ("E", "F", 35),
         ("E", "H", 200),
         ('E', 'I', 115),
         ('E', 'J', 500),
         ('F', 'I', 250),
         ('H', 'J', 160),
         ('H', 'K', 125),
         ('I', 'J', 80),
         ('I', 'L', 180),
         ("J", "K", 75),
         ("J", "L", 720),
         ("J", "M", 320),
         ("K", "M", 350),
         ("L", "M", 420),
        ]
# Ajout des arêtes pondérés
for edge in edges:
    G3.add_edge(edge[0], edge[1], weight=edge[2])

options = {
    "font_size": 8,
    "node_size": 1000,
    "edgecolors": "#4682B4",
    "alpha": 0.95,
    "linewidths": 2,
    "width": 2,
}

import heapq

def dijkstra(graph, start):
    # les dictionnaires des prédécesseurs et des distances
    p = {node:None for node in graph}
    d = {node:float('infinity') for node in graph}
    d[start] = 0
    f = [(0, start)]
    while len(f) > 0:
        current_distance, current_node = heapq.heappop(f)
        for neighbor in graph.neighbors(current_node):
            distance = current_distance + graph[current_node][neighbor]['weight']
            # on considère ce noeud si sa distance est inférieure à celle existante
            if distance < d[neighbor]:
                d[neighbor] = distance
                p[neighbor] = current_node
                heapq.heappush(f, (distance, neighbor))
    return p, d  

depart = 'A'
predecessors, distances = dijkstra(G3, depart)


pos = nx.spring_layout(G3, seed=1234)
edge_labels = nx.get_edge_attributes(G3,'weight')
color_map=['#e06000' if node==depart else '#A0CBE2' for node in G3]
labels={node:node+"="+str(distances[node]) for node in G3.nodes()}
plt.figure(figsize=(8,5))
nx.draw(G3, pos, labels=labels, node_color=color_map, **options)
edgelist = [(node, pred) for node, pred in predecessors.items() if pred]
nx.draw_networkx_edges(
    G3,
    pos,
    edgelist=edgelist,
    width=8,
    alpha=0.5,
    edge_color="#e06000",
)
nx.draw_networkx_edge_labels(G3, pos, edge_labels = edge_labels)
plt.axis('off')
plt.show()

