# Exercice 1
def moyenne(liste):
    '''
    renvoie la moyenne pondérée de la liste
    liste : couple de notes et de coefficients
    '''
    assert isinstance(liste, list); return sum([i[0] * i[1] for i in liste])/sum([j[1] for j in liste])

print(moyenne([(15,2),(9,1),(12,3)]))

# Exercice 2
def pascal(n):
    C = [[1]]
    for k in range(1,n+1):
        Ck = [1]
        for i in range(1,k):
            Ck.append(C[k-1][i-1]+C[k-1][i])
        Ck.append(1)
        C.append(Ck)
    return C

assert pascal(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
assert pascal(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]