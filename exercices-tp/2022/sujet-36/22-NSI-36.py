# Exercice 1
def recherche(tab, n):
    '''
    Renvoie l'indice de la dernière occurence de n dans tab
    si n non trouvé, renvoie la longueur de tab
    '''
    assert type(tab) == list
    assert type(n) == int
    
    if n not in tab:
        return len(tab)
    for i in range(len(tab)-1,-1,-1):
        if tab[i] == n:
            return i

print(recherche([5, 3],1))
print(recherche([2, 4],2))
print(recherche([2, 3, 5, 2, 4],2))

# Exercice 2
from math import sqrt   # import de la fonction racine carree

def distance(point1, point2): 
    """ Calcule et renvoie la distance entre deux points. """
    return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

assert distance((1, 0), (5, 3)) == 5.0, "erreur de calcul"

def plus_courte_distance(tab, depart):
    """ Renvoie le point du tableau tab se trouvant a la plus     
    courte distance du point depart."""
    point = tab[0]
    min_dist = distance(point,depart)
    for i in range (1, len(tab)):
        if distance(tab[i], depart) < min_dist:
            point = tab[i]
            min_dist = distance(tab[i], depart)
    return point

assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (0, 0)) == (2, 5), "erreur"
