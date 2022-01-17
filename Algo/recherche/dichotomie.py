def rechercherec( element, liste_triee, a = 0, b = -1 ):
    if a == b : 
        return a
    if b == -1 : 
        b = len(liste_triee)-1
    m = (a+b)//2
    if liste_triee[m] == element :
        return m
    elif liste_triee[m] > element :
        return rechercherec(element, liste_triee, a, m-1)
    else :
        return rechercherec(element, liste_triee, m+1, b)

print(rechercherec(4, [1,2,3,4,5,6,7,8,9]))
