from tri import *
from comparaison import *
from random import shuffle
from time import process_time
from prettytable import PrettyTable

def comparer_table(f1, f2):
	"""
	Compares the time between two sorting functions in a table
	"""
	x = PrettyTable()
	x.field_names = ["Elements", "Function 1 time (ms)", "Function 2 time (ms)"]

	x.add_rows(comparer(f1, f2))
	return x
