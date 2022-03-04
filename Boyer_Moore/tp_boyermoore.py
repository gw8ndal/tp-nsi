def pretraitement(motif):
    """
    Retourne la table de sauts pour les différentes lettres du motif (on exclu la dernière lettre)"""
    table = {}
    for i, letter in enumerate(motif[:-1]):
        table[letter]=len(motif)-i-1
    return table

def cherche_motif(motif, texte):
    """
    Cherche un motif dans un texte
    Retourne Vrai si le motif est trouvé, faux sinon
    """

    def __comparer(i,j):
        if i == j:
            return True
        else:
            return False

    T = len(texte)
    M = len(motif)
    # On crée la table des sauts
    sauts = pretraitement(motif)
    # Si le motif est plus long que le texte on retourne False
    if M > T:
        return False

    # On commence à l'indice de la dernière lettre du motif
    i = M-1
    decalage = 0
    while i<T:
        
    
        i += 1
    return False

### vérification
motif = 'CGGCAG'
mot   = 'CAATGTCTGCACCAAGACGCCGGCAGGTGCAGACCTTCGTTATAGGCGATGATTTCGAACCTACTAG'

table = pretraitement('CGGCAG')
print(table)
print(cherche_motif(motif, mot))
