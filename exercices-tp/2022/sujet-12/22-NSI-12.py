# Exercice 1
def moyenne(tab):
    '''
    Renvoie la moyenne de tab
    tab : liste de nombres
    '''
    if tab == []:
        return 'erreur'
    a = 0
    for i in tab:
        a += i
    return a / len(tab)

assert moyenne([5,3,8]) == 5.333333333333333
assert moyenne([1,2,3,4,5,6,7,8,9,10]) == 5.5
assert moyenne([]) = 'erreur'

# Exercice 2
def tri(tab):
    #i est le premier indice de la zone non triee, j le dernier indice. 
    #Au debut, la zone non triee est le tableau entier.
    i= 0
    j= len(tab) - 1
    while i != j :
        if tab[i]== 0:
            i += 1
        else :
            valeur = tab[j]
            tab[j] = 1
            tab[i] = valeur
            j -= 1
    return tab

assert tri([0,1,0,1,0,1,0,1,0]) == [0, 0, 0, 0, 0, 1, 1, 1, 1]