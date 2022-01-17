# Tri par insertion

def tri_insertion(tab):
	for i in range(1, len(tab)):
		k = tab[i]
		j = i-1
		while j >= 0 and k < tab[j]:
			tab[j + 1] = tab[j]
			j -= 1
		tab[j + 1] = k
	return tab

# Tri fusion

def fusion(t1,t2):
	if t1==[]:
		return t2
	elif t2==[]:
		return t1
	elif t1[0]<t2[0]:
		return [t1[0]]+fusion(t1[1:],t2)
	else:
		return [t2[0]]+fusion(t1,t2[1:])


def tri_fusion(t):
	n=len(t)
	if n<2:
		return t
	else:
		m=n//2
		return fusion(tri_fusion(t[:m]),tri_fusion(t[m:]))
