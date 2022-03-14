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



def rendu_monnaie_memo(P,x, memo = None):
    """
    Détermine le nombre minimal de pièces
    à rendre.

    Algorithme récursif avec mémoïsation.
    """
    if memo is None:
        memo = {0:0}
    # A CODER



print(rendu_monnaie_brute(P, 11)) # Méthode bourrine
print(rendu_monnaie_memo(P, 171)) # Pour les gigachad