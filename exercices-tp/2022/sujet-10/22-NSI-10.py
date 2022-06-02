# Exercice 1
def occurence_lettres(phrase):
    '''
    Renvoie un dictionnaire avec les lettres et leurs occurences correspondantes
    phrase : chaine de caractères
    '''
    dico = {}
    for i in phrase:
        if i in dico:
            dico[i] += 1
        else:
            dico[i] = 1
    return dico

assert occurence_lettres('Hello world !') == {'H': 1,'e': 1,'l': 3,'o': 2,' ': 2,'w': 1,'r': 1,'d': 1,'!': 1}

# Exercice 2
def fusion(L1,L2):
    n1 = len(L1)
    n2 = len(L2)
    L12 = [0]*(n1+n2)
    i1 = 0
    i2 = 0
    i = 0
    while i1 < n1 and i2 < n2:
        if L1[i1] < L2[i2]:
            L12[i] = L1[i1]
            i1 += 1
        else:
            L12[i] = L2[i2]
            i2 += 1
        i += 1
    while i1 < n1:
    	L12[i] = L1[i1]
    	i1 = i1 + 1
    	i += 1
    while i2 < n2:
    	L12[i] = L2[i2]
    	i2 = i2 + 1
    	i += 1
    return L12

assert fusion([1,6,10],[0,7,8,9]) == [0, 1, 6, 7, 8, 9, 10]