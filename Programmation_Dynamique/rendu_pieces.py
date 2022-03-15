P = [2, 5, 10, 20, 50, 100] # On déclare les pièces à utiliser

def rendu_monnaie_brute(P,x):
    """
    Détermine le nombre minimal de pièces
    à rendre.
    Algorithme récursif.
    """
    if x == 0:
        return 0

    nb_min = float('inf')

    if x > max(P):
        return None
    for i in P:
        if i <= x:
            nb_piece = 1 + rendu_monnaie_brute(P, x - i)
            if nb_piece < nb_min:
                nb_min = nb_piece
    return nb_min



def rendu_monnaie_smart(P,x, memo = None, p_util = None):
    """
    Détermine le nombre minimal de pièces
    à rendre.

    Algorithme récursif avec mémoïsation.
    """
    if memo is None:
        memo = {0:0}
    if p_util is None:
        p_util = []
    if x == 0:
        return 0
    if  x in memo.keys():
        return memo[x]
    nb_min = float('inf')

    for i in P:
        if i <= x:
            nb_piece = 1 + rendu_monnaie_smart(P, x - i, memo, p_util)[0]
            if nb_piece < nb_min:
                nb_min = nb_piece
                memo[x] = nb_min
                p_util.append(i)
    return nb_min, p_util


import sys
sys.setrecursionlimit(100000)

print(rendu_monnaie_brute(P, 11)) # Méthode bourrine
print(rendu_monnaie_smart(P, 171)) # Pour les gigachad