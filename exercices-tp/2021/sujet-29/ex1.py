def calcul(n, res = []):
	assert type(n) == int # Vérifier que n est un entier
	if n > 1:
		if n%2 == 0:
			n = n//2
			res.append(n)
			calcul(n)
		else:
			n = n*3 + 1
			res.append(n)
			calcul(n)
	return res
