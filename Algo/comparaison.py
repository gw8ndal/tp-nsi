from tri import *
from random import shuffle
from time import process_time

def comparer(f1, f2):
	"""
	Compares the time between two sorting functions
	"""
	result = []
	for i in range(10, 1000, 10):
		elm = [e for e in range(i)]
		shuffle(elm)

		time1_start = process_time()*1000
		f1(elm)
		time1_end = process_time()*1000
		time2_start = process_time()*1000
		f2(elm)
		time2_end = process_time()*1000
		time1 = time1_end - time1_start
		time2 = time2_end - time2_start

		result.append([i, time1, time2])
	return result
