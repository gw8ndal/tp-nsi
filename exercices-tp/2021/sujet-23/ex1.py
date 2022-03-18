def occurence_lettres(phrase):
	assert type(phrase) == str
	dico = {}
	for i in phrase:
		if i in dico.keys():
			dico[i] += 1
		else:
			dico[i] = 1
	return dico

print(occurence_lettres('Hello World !'))
