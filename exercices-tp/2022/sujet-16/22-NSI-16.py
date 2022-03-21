def maxi(tab):
    """
    Prend en paramètre une liste tab de nombres entiers et
    renvoie un couple donnant le plus grand élément de cette liste, ainsi que l’indice de la
    première apparition de ce maximum dans la liste. Si la liste est vide, retourne None
    """
    assert type(tab) == list
    
    if tab == []:
        return None
    
    return sorted(tab)[-1], tab.index(sorted(tab)[-1])

print(maxi([1,5,6,9,1,2,3,7,9,8]))
print(maxi([]))

def positif(T):
    T2 = list(T)
    T3 = []
    while T2 != []:
        x = T2.pop()
        if x >= 0:
            T3.append(x)
    T2 = []
    while T3 != []:
        x = T3.pop()
        T2.append(x)
    print('T = ',T)
    return T2

positif([-1,0,5,-3,4,-6,10,9,-8 ])