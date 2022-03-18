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

def recherche_max_brute(p):
    """
    Recherche du chemin optimal parmi tous les chemins possibles
    """
    s = p[0][0]
    if len(p) == 1:
        return s
    else:
        p_gaucho = sous_pyramide_gauche(p)
        p_facho = sous_pyramide_droite(p)
        return s + max(recherche_max_brute(p_gaucho), recherche_max_brute(p_facho))

def build_max_pyramide_recursif(p, line = 0):
    """
    Retourne la pyramide p_max ( p est modifiée 'in place' )
        4                4
       9 1             13 5
      1 2 9    =>    14 15 14
     1 7 9 1        15 22 24 15
    line : le numéro de ligne
    """
    # Si on ne se trouve pas au sommet
    if line != 0:
        # Pour la première case de la ligne courante, on ajoute la première case de la ligne du dessus
        p[line][0] += p[line-1][0]
        # Pour la dernière case de la ligne courante, on ajoute la dernière case de la ligne du dessus
        p[line][-1] += p[line-1][-1]
        # On parcourt toutes les autres cases et on y ajoute le plus grand contenu des deux cases supérieures
        for i in range(1,line):
            p[line][i] += max(p[line-1][i-1], p[line-1][i])
            
    # Cas général : nous ne sommes pas à la dernière ligne 
    if line < len(p) - 1:
        return build_max_pyramide_recursif(p, line+1)
    # Cas d'arrêt : on est arrivé à la dernière ligne
    else:
        return p

def build_max_pyramide_iteratif(p):
    """
    Retourne la pyramide p_max ( p est modifiée 'in place' )
        4                4
       9 1             13 5
      1 2 9    =>    14 15 14
     1 7 9 1        15 22 24 15
    line : le numéro de ligne
    """
    for line in range(1, len(p)):

        p[line][0] += p[line - 1][0]
        p[line][-1] += p[line - 1][-1]
        for i in range(1, line - 1):
                p[line][i] += max(p[line - 1][i - 1], p[line - 1][i])

    return p


p = generer_pyramide(6)
enorme_p = generer_pyramide(20)
afficher_pyramide(p)

# afficher_pyramide(sous_pyramide_gauche(p))

# afficher_pyramide(sous_pyramide_droite(p))

#print(recherche_max_brute(enorme_p))
afficher_pyramide(build_max_pyramide_iteratif(p))