from tri_fusion import *
from tri_insert import *
from time import process_time
from random import shuffle
def comparer(f1, f2):
	for i in range(1000, 100000, 100):
		elm = [e for e in range(i)]
		shuffle(elm)

		time1_debut = process_time()
		f1(elm)
		time1_fin = process_time()
		time1 = time1_fin - time1_debut

		time2_debut = process_time()
		f2(elm)
		time2_fin = process_time()
		time2 = time2_fin - time2_debut

		return time1, time2



print(comparer(tri_fusion, tri_insert))
