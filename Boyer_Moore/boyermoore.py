import requests


def pretraitement(motif):
    """
    Retourne la table de sauts pour les différentes lettres du motif (on exclu la dernière lettre)"""
    table = {}
    for i, letter in enumerate(motif[:-1]):
        table[letter]=len(motif)-i-1
    return table

def cherche_motif(motif, texte, mode = 0):
    """
    Cherche un motif dans un texte
    Retourne Vrai si le motif est trouvé ou si il est vide, faux sinon
    """
    T = len(texte)
    M = len(motif)
    occurence = 0
    # On crée la table des sauts
    sauts = pretraitement(motif)
    # Si le motif est plus long que le texte on retourne False
    if M > T:
        if mode == 0:
            return False
        else:
            return 0
    if motif == '':
        if mode == 0:
            return False
        elif mode == 1:
            return 0

    # On commence à l'indice de la dernière lettre du motif
    i = M-1
    j = M-1
    while j<T:
        i = M-1
        k = j
        while i >= 0 and texte[k] == motif[i]:
            i -= 1
            k -= 1
        if i >= 0:
            if texte[k] in motif[:-1]:
                j += sauts[texte[k]]
            else:
                j += M
        else:
            if texte[k] in motif[:-1]:
                j += sauts[texte[k]]
            else:
                j += M 
            
            if mode == 0:
                return True
            elif mode == 1:
                occurence += 1
    if mode == 0:
        return False
    elif mode == 1:
        return occurence

### vérification
motif = 'CGGCAG'
mot = 'CAATGTCTGCACCAAGACGCCGGCAGGTGCAGACCTTCGTTATAGGCGATGATTTCGAACCTACTAG'

## Assert V 1.0
assert cherche_motif(motif, mot) == True
assert cherche_motif('dab', 'abracadabra') == True, "'%s' devrait ếtre dans '%s'"%(motif, texte)
assert cherche_motif('zebi', '') == False
assert cherche_motif('', 'abracadabra') == False
assert cherche_motif('abracadabra', 'cad') == False

## Assert V 1.1
assert cherche_motif('dab', 'abracadabra ahmdoullah abracadabra', 1) == 2
assert cherche_motif('zebi', '') == 0
assert cherche_motif('', 'abracadabra') == 0
assert cherche_motif('abracadabra', 'cad') == 0


data  = requests.get("https://www.gutenberg.org/files/84/84-0.txt").text
print(cherche_motif('Frankenstein', data, 1))
