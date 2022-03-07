import requests

def pretraitement(motif):
    """
    Retourne la table de sauts pour les différentes lettres du motif (on exclu la dernière lettre)"""
    table = {}
    for i, letter in enumerate(motif[:-1]):
        table[letter]=len(motif)-i-1
    return table

def cherche_motif(motif, texte, mode=0):
    """
    Cherche un motif dans un texte
    Retourne Vrai si le motif est trouvé, faux sinon. Si le motif est vide, retourne False 
    """
    T = len(texte)
    M = len(motif)
    # On crée la table des sauts
    sauts = pretraitement(motif)
    occ = 0
    # Si le motif est plus long que le texte on retourne False
    if M > T:
        if mode == 0:
            return False
        else:
            return occ
    if motif == '':
        if mode == 0:
            return False
        elif mode == 1:
            return 0
    nb = 0
    lst = []
    # On commence à l'indice de la dernière lettre du motif
    i = M-1 # dans le motif
    j = M-1 # dans le texte
    while j<T:
        i = M-1
        k = j
        while texte[k] == motif[i] and i >= 0:
            i -= 1
            k -= 1
        if i >= 0:
            if texte[k] in motif[:-1]:
                j = j + sauts[texte[k]]
            else:
                j += M
        else:
            if texte[k] in motif[:-1]:
                j = j + sauts[texte[k]]
            else:
                j += M

            if mode == 0:
                return True
            elif mode == 1:
                occ += 1
    if mode == 0:
        return False
    elif mode == 1:
        return occ

### vérification
motif = 'Frankenstein'
texte = requests.get("https://www.gutenberg.org/files/84/84-0.txt").text.replace(" ", "")
print(cherche_motif(motif, texte, 1))

# Tests mode 0
assert cherche_motif("dab", "abracadabra") == True
assert cherche_motif("zebi", " ") == False
assert cherche_motif("", "abracadabra") == False
assert cherche_motif("abracadabra", "cad") == False
assert cherche_motif("", "") == False

# Tests mode 1
assert cherche_motif("dab", "abracadabradabra", 1) == 2
assert cherche_motif("zebi", " ", 1) == 0
assert cherche_motif("", "abracadabra", 1) == 0
assert cherche_motif("abracadabra", "cad", 1) == 0
assert cherche_motif("", "", 1) == 0
