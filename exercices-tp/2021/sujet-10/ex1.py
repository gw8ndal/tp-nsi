def maxi(tab):
	nmaxi = 0
	index_max = 0
	for i in range(len(tab)):
		if tab[i] > nmaxi:
			nmax, index_max = tab[i], i
	return nmaxi, index_max
