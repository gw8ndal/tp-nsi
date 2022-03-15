from random import randint
def generer_pyramide(h):
    """
    Retourne une pyramide de hauteur h contenant des nombres aléatoires entre 1 et 9
    """
    pyramide = []
    for i in range(1, h+1):
        pyramide.append([randint(1, 9) for i in range(i)])
    return pyramide

def afficher_pyramide(p):
    """
    Affiche la pyramide p
    """
    for i in p:
        espaces = (len(p) - len(i))*' '
        print(espaces + ' '.join([str(j) for j in i]))



def sous_pyramide_gauche(p):
    gaucho = [l[:-1] for l in p if len(l) > 1]
    return gaucho 

def sous_pyramide_droite(p):
    facho = [l[1:] for l in p if len(l) > 1]
    return facho

p = generer_pyramide(5)
afficher_pyramide(p)

afficher_pyramide(sous_pyramide_gauche(p))


afficher_pyramide(sous_pyramide_droite(p))