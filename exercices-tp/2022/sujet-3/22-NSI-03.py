# Exercice 1
def delta(tab):
    """
    renvoie un tableau en remplaçant les valeurs par la différence avec la valeur précédente
    """
    assert tab != []
    l = [tab[0]]
    for i in range(1, len(tab)):
        l.append(tab[i] - tab[i-1])
    return l

print(delta([1000, 800, 802, 1000, 1003]))
print(delta([42]))

# Exercice 2
class Noeud:
    def __init__(self, g, v, d):
        self.gauche = g
        self.valeur = v
        self.droit = d
    
    def __str__(self):
        return str(self.valeur)
    
    def est_une_feuille(self):
        '''Renvoie True si et seulement si le noeud est une feuille'''
        return self.gauche is None and self.droit is None

def expression_infixe(e):
    s = ''
    if e.gauche is not None:
        s = '(' + s + expression_infixe(e.gauche)
    s = s + str(e.valeur)
    if e.droit is not None:
        s = s + expression_infixe(e.droit) + ')'
    if e.est_une_feuille :
        return s


e = Noeud(Noeud(Noeud(None, 3, None), '*', Noeud(Noeud(None, 8, None),'+', Noeud(None, 7, None))), '-', Noeud(Noeud(None, 2, None), '+',Noeud(None, 1, None)))
print(expression_infixe(e))