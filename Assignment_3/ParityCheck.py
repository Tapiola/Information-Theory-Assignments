import sys
import numpy as np
from StandardForm import gauss_elimination

def destandartise (ms, ls):
	for i in range (len (ls)):
		while not ls[i]-1 == i:
			ms[:, [ls[i]-1,i]] = ms[:, [i,ls[i]-1]]
			ls[ls[i]-1], ls[i] = ls[i], ls[ls[i]-1]
	return ms

def parity_check (ms, k, n):
	ms, ls = gauss_elimination (ms, k, n)
	ms = np.concatenate ([ms[:, k:n].transpose(), np.identity (n-k, dtype=int)], axis=1)
	ms = destandartise (ms, ls)
	return ms

def parity (name1, name2):
	file1 = open (name1, "r")
	read_ls = file1.readlines()
	file1.close ()
	new_ls = []
	n, k = map (int, read_ls[0].split ())
	
	for e in read_ls[1:]:
		new_ls += [int (c) for c in e if not c == '\n']
	
	ms = np.matrix (new_ls).reshape ((k, n))

	ms = parity_check (ms, k, n)
	file2 = open (name2, "w")
	file2.write (str (n) + ' ' + str (n-k))
	for s in np.char.mod('%s', ms):
		file2.write ('\n' + ''.join (s))
	file2.close ()
				
if __name__ == "__main__":
	parity (sys.argv[1], sys.argv[2])