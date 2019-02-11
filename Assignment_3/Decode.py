import sys
import numpy as np
from NewRead import file_reader, bytes_to_binary
from NewWrite import byte_writer
from ParityCheck import parity_check
import json

def matrix_to_string (m):
	st = ''
	for s in np.char.mod('%s', m):
		st += ''.join (s)
	return st

def parser (name):
	file = open (name, "r")
	d = json.loads (file.read ())
	pc_k = list (d.keys())[0]
	n, k = d[pc_k]
	d.pop (pc_k)

	new_ls = [int (c) for c in pc_k]
	
	pc = np.matrix (new_ls).reshape ((k, n))	
	file.close ()
	return pc, d, n, k


def decoder (name1, name2, name3):
	pc, table, n, k = parser (name1)

	read_bytes = file_reader (name2)
	data = bytes_to_binary (read_bytes)
	new_binary = ''
	for i in range (n, len (data) + n, n):
		code_str = data[i-n:i]
		code = np.matrix ([int (c) for c in code_str])
		synd = matrix_to_string (pc.dot (code.T) % 2)

		if synd in table:
			e = np.matrix ([int (c) for c in table[synd]]).reshape (n,)
			code = (e + code) % 2
			code_str = matrix_to_string (code)
		new_binary += code_str

	byte_writer (name3, new_binary)

if __name__ == "__main__":
	decoder (sys.argv[1], sys.argv[2], sys.argv[3])