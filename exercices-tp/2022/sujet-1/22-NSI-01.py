def recherche(caractere, mot):
    '''
    renvoie le nombre d’occurrences de caractere dans mot,
    c’est-à-dire le nombre de fois où caractere apparaît dans mot.
    
    '''
    assert type(caractere) == str
    assert type(mot) == str
    assert len(caractere) == 1

    o = 0
    for i in mot:
        if caractere == i:
            o += 1
    return o

print(recherche('e', "sciences"))
print(recherche('i',"mississippi"))
print(recherche('a',"mississippi"))


Pieces = [100,50,20,10,5,2,1]
def rendu_glouton(arendre, solution=[], i=0):
    if arendre == 0:
        return solution
    p = Pieces[i]
    if p <= arendre :
        solution.append(p)
        return rendu_glouton(arendre - p, solution, i)
    else :
        return rendu_glouton(arendre, solution, i+1)

print(rendu_glouton(68,[],0))
print(rendu_glouton(291,[],0))