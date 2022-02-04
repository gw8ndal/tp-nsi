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
for edge in edges:
    G1.add_edge(edge[0], edge[1])

def cycle_search(g, sommet, lst_sommet = None):
    if lst_sommet == None:
        lst_sommet = []
    for i in g.neighbors(sommet):
        if i not in lst_sommet:
            lst_sommet.append(i)
            cycle_search(g, i, lst_sommet)
        else:
            return True
    return False

print(cycle_search(G1, 'A'))