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
    Retourne Vrai si le motif est trouvé, faux sinon
    """
   
    n = 0
    T = len(texte)
    M = len(motif)
    # On crée la table des sauts
    sauts = pretraitement(motif)
   
    if motif =='':
        if mode == 0:
            return False
        elif mode == 1 :
            return n
   
    # Si le motif est plus long que le texte on retourne False
    if M > T:
        if mode == 0:
            return False
        elif mode == 1 :
            return n
      # On commence à l'indice de la dernière lettre du motif
    i = M-1
    while i<T:
        letter = texte[i]
        if letter == motif[-1] :
            if texte[i-M+1:i+1] == motif :
                if mode == 0:
                    return True
                elif mode == 1 :
                    n = n + 1
        if letter in sauts.keys():
            i += sauts[letter]
        else :
            i+=1
    if mode == 0:
        return False
    elif mode == 1 :
        return n

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


data  = requests.get("https://www.gutenberg.org/files/84/84-0.txt")
data.encoding = 'utf-8'
print(cherche_motif('.', data.text.lower(), 1))