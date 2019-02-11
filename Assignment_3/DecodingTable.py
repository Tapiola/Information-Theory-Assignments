import sys
import numpy as np
from ParityCheck import parity_check
import json

def matrix_to_string (m):
	st = ''
	for s in np.char.mod('%s', m):
		st += ''.join (s)
	return st

def generate_errors (e, n, num, pc, table):
	num -= 1
	for i in range(n):
		if e[i,] == 1:
			continue
		e[i,] = 1
		key = matrix_to_string (pc.dot(e.T) % 2)
		if not key in table:
			table[key] = matrix_to_string (e)
		if num > 0:
			generate_errors (e, n, num, pc, table)
		e[i,] = 0

def decoding_table (name1, name2, name3):
	file1 = open (name1, "r")
	read_ls = file1.readlines ()
	file1.close ()
	new_ls = []
	n, k = map (int, read_ls[0].split ())
	
	for e in read_ls[1:]:
		new_ls += [int (c) for c in e if not c == '\n']
	
	ms = np.matrix (new_ls).reshape ((k, n))	

	file2 = open (name2, "r")
	num = int (file2.readlines ()[0])
	file2.close ()

	pc = parity_check (ms, k, n)

	e = np.zeros ((n,), dtype=int)
	table = {}
	generate_errors (e, n, num, pc, table)

	file3 = open (name3, "w")
	file3.write ('{\n')

	file3.write ('\"' + matrix_to_string (pc))
	file3.write ('\":[' + str (n) + ', ' + str (n-k) + ']')
	for key in table:
		file3.write (',\n\"' + key + '\":\"' + table[key] + '\"')

	file3.write ('\n}')
	file3.close ()


if __name__ == "__main__":
	decoding_table (sys.argv[1], sys.argv[2], sys.argv[3])