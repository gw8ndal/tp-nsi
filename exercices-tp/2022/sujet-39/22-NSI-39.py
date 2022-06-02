# Exercice 1
def moyenne(liste):
    '''
    Renvoie la moyenne des valeurs de la liste
    '''
    assert type(liste) == list
    return sum([i for i in liste])/len(liste)

print(moyenne([10,20,30,40,60,110]))

# Exercice 2
coeur = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0], \
        [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0], \
        [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0], \
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], \
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], \
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], \
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0], \
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

CARACTERES = ['  ', ' *']

def affiche(dessin):
    for ligne in dessin:
        for digit in ligne:
            print(CARACTERES[digit], end="")
        print()


def zoom_liste(liste_depart, k):
    '''renvoie une liste contenant k fois chaque 
    élément de liste_depart'''
    liste_zoom = []
    for elt in liste_depart:
        for i in range(k):
            liste_zoom.append(elt)
    return liste_zoom

def zoom_dessin(grille, k):
    '''renvoie une grille où les lignes sont zoomées k fois 
    ET répétées k fois'''
    grille_zoom = []
    for ligne in grille:
        liste_zoom = zoom_liste(ligne, k)
        for i in range(k):
            grille_zoom.append(liste_zoom)
    return grille_zoom
