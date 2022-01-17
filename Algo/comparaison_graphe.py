import matplotlib.pyplot as plt
from comparaison import *
from tri import *

def comparer_graphe(f1, f2):
    result = comparer(f1, f2)
    plt.figure(figsize=(10, 10))
    x = [r[0] for r in result]
    y1 = [r[1] for r in result]
    y2 = [r[2] for r in result]
    plt.scatter(x, y1, label='Function 1')
    plt.scatter(x, y2, label='Function 2')
    plt.xlabel('Elements in list')
    plt.ylabel("Time (ms)")
    plt.legend()
    plt.grid(True)
    return plt.show()
    
