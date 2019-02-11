import sys
import numpy as np
from NewWrite import file_reader, bytes_to_binary, byte_writer
from StandardForm import gauss_elimination

def matrix_to_string (m):
	st = ''
	for s in np.char.mod('%s', m):
		st += ''.join (s)
	return st

def decoder (name1, name2, name3):
	file1 = open (name1, "r")
	read_ls = file1.readlines()
	file1.close ()
	new_ls = []
	n, k = map (int, read_ls[0].split ())
	
	for e in read_ls[1:]:
		new_ls += [int (c) for c in e if not c == '\n']
	
	ms = np.matrix (new_ls).reshape ((k, n))

	read_bytes = file_reader (name2)
	data = bytes_to_binary (read_bytes)
	new_binary = ''

	for i in range (k, len (data) + k, k):
		code_str = data[i-k:i]
		code = np.matrix ([int (c) for c in code_str])
		new_binary += matrix_to_string (code.dot (ms) % 2)

	byte_writer (name3, new_binary)

if __name__ == "__main__":
	decoder (sys.argv[1], sys.argv[2], sys.argv[3])