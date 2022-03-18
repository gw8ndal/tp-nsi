def recherche(elt, tab):
	indices = []
	for i in range(len(tab)):
		if elt == tab[i]:
			indices.append(i)
	return indices
