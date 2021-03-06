import matplotlib.pyplot as plt
import networkx as nx
# Instantiation d'un graphe
G1 = nx.Graph()
edges = [('A', 'B'),
         ('A', 'C'),
         ('A', 'D'),
         ('B', 'E'),
         ('C', 'F'),
         ('C', 'I'),
         ('D', 'G'),
         ('B', 'H'),
         ('H', 'I'),
         ('F', 'J'),
         ('E', 'K'),
         ('K', 'G'),
         ('J', 'L'),
        ]
options = {
    "font_size": 8,
    "node_size": 1000,
    "edgecolors": "#4682B4",
    "alpha": 0.95,
    "linewidths": 2,
    "width": 2,
}

# Ajout des arêtes pondérés
for edge in edges:
    G1.add_edge(edge[0], edge[1])

def show_graph(): # affiche le graph avec graphviz et networkx
    plt.figure(figsize=(5,3))
    pos = nx.nx_agraph.graphviz_layout(G1)
    color_map=['#A0CBE2' for node in G1]
    #color_map=['#FFA500' if node=='A' else '#A0CBE2' for node in G]
    nx.draw(G1, pos, node_color=color_map, with_labels=True, **options)
    plt.show()
# show_graph()

def BFS(graph, node): # recherche d'un sommet dans le graph
    f = [node]
    distance={node:0}
    while len(f)>0:
        current_node = f.pop()
        g_neighbors = graph.neighbors(current_node)
        for i in g_neighbors:
            if i not in distance.keys():
                f.insert(0, i)
                distance[i] = distance[current_node] + 1
    return distance
#BFS(G1, 'L')

def parcours_chemin(graph, node): # trouver par quels sommets il faut passer pour faire un chemin court
    if node not in graph.nodes:
        return {}
    f = [node]
    parcours={node:None}
    while len(f)>0:
        current_node = f.pop()
        g_neighbors = graph.neighbors(current_node)
        for i in g_neighbors:
            if i not in parcours.keys():
                f.insert(0, i)
                parcours[i] = current_node
    return parcours

# print(parcours_chemin(G1, 'J'))

def chemin(G, start, end):
    predecesseurs = parcours_chemin(G, start)
    if not predecesseurs or end not in G.nodes:
        return []
    current = end
    path=[current]
    while current != start:
        predecesseur = predecesseurs.get(current)
        if predecesseur:
            path.insert(0, predecesseur)
            current = predecesseur
    return path

# print(chemin(G1, 'L', 'K'))

path=chemin(G1, "L", "G")
print(path)
plt.figure(figsize=(4,3))

pos = nx.nx_agraph.graphviz_layout(G1)
color_map=['#FFA500' if node in path else '#A0CBE2' for node in G1]
nx.draw(G1, pos, node_color=color_map, with_labels=True, **options)

plt.show()