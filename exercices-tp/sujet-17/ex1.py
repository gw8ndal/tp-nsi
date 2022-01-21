def indice_du_min(tab):
    """
    Renvoie l'indice du minimum de la liste donnée
    """
    assert type(tab) == list
    tmp = [i for i in tab]
    while len(tmp) > 1:
        if tmp[0] > tmp[1]:
            tmp.pop(0)
        else:
            mini = tmp[0]
            tmp.pop(1)
    if len(tmp) == 1:
        mini = tmp[0]
    return tab.index(mini)

# Méthode alternative
def indice_du_min2(tab):
	return tab.index(min(tab))

print(indice_du_min([5]))
print(indice_du_min([2, 4, 1]))
print(indice_du_min([5, 3, 2, 2, 4]))


print(indice_du_min2([5]))
print(indice_du_min2([2, 4, 1]))
print(indice_du_min2([5, 3, 2, 2, 4]))
