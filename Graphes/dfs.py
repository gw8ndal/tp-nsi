import matplotlib.pyplot as plt
import networkx as nx

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

def DFS_rec(g, noeud, noeuds_visites=None):
    if noeuds_visites == None:
        noeuds_visites = []
    if noeud not in noeuds_visites:
        noeuds_visites.append(noeud)
        for voisin in g.neighbors(noeud):
            DFS_rec(g, voisin, noeuds_visites)
    return noeuds_visites

print(DFS_rec(G1, "A"))