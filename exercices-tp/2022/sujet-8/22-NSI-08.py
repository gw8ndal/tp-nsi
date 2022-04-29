# Exercice 1
def recherche(elt, tab):
    """Renvoie l'indice de la première occurence de elt dans tab

    Args:
        elt (int): élément à rechercher
        tab (list): liste d'éléments
    """
    assert type(elt) == int, 'elt doit être un entier'
    assert type(tab) == list, 'tab doit être une liste'

    for i in range(len(tab)):
        if tab[i] == elt:
            return i
    return -1

print(recherche(1, [2, 3, 4]))
print(recherche(1, [10, 12, 1, 56]))
print(recherche(50, [1, 50, 1]))
print(recherche(15, [8, 9, 10, 15]))

# Exercice 2
def insere(a, tab):
    l = list(tab) #l contient les mêmes éléments que tab
    l.append(a)
    i = len(l) - 2
    while a < l[i] and i >= 0:
        l[i+1] = l[i]
        l[i] = a
        i -= 1
    return l

print(insere(3,[1,2,4,5]))
print(insere(10,[1,2,7,12,14,25]))
print(insere(1,[2,3,4]))