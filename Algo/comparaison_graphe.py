import matplotlib as plt
from comparaison import *

def comparer_graphe(f1, f2):
    result = comparer(f1, f2)
    plt.figure(figsize=(10, 10))
    x = [r[0] for r in results]
    y1 = [r[1] for r in results]
    y2 = [r[1] for r in results]
    plt.scatter(x, y1, label='Function 1')
    plt.scatter(x, y2, label='Function 2')
    plt.xlabel('Elements in list')
    plt.ylabel("Time (ms)")
