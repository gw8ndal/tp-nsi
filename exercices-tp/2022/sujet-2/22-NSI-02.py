def moyenne(liste):
    '''
    renvoie la moyenne pondérée de la liste
    liste : couple de notes et de coefficients
    '''
    return sum([i[0] * i[1] for i in liste])/sum([j[1] for j in liste])
    # return sum([i[0] * i[1] for i in liste])/sum([j[0] for j in liste])

print(moyenne([(15,2),(9,1),(12,3)]))


def pascal(n):
    C= [[1]]
    for k in range(1,...):
        Ck = [...]
        for i in range(1,k):
            Ck.append(C[...][i-1]+C[...][...] )
        Ck.append(...)
        C.append(Ck)
    return C
