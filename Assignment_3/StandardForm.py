import sys
import numpy as np


def gauss_elimination (ms, k, n):
	ls = list (range (1, n+1))
	for i in range (k):	
		if ms[i,i] == 0:
			is_row = False
			for ki in range (i+1, k):
				if not ms[ki,i] == 0:
					is_row = True
					ms[[ki,i], :] = ms[[i,ki], :]
					break
			if not is_row: 
				for ki in range (i+1, n):
					if not ms[i,ki] == 0:
						ms[:, [i,ki]] = ms[:, [ki,i]]
						ls[i], ls[ki] = ls[ki], ls[i]
						break

		if not ms[i,i] == 0 and not ms[i,i] == 1:
			ms[i, :] = ms[i, :]/ms[i,i]

		if ms[i,i] == 1:
			for ki in range (k):
				if not ki == i:
					ms[ki, :] = abs (ms[ki, :] - ms[i, :] * ms[ki,i])
	return ms, ls


def standartise (name1, name2):
	file1 = open (name1, "r")
	read_ls = file1.readlines()
	file1.close ()
	new_ls = []
	n, k = map (int, read_ls[0].split ())
	
	for e in read_ls[1:]:
		new_ls += [int (c) for c in e if not c == '\n']
	
	ms = np.matrix (new_ls).reshape ((k, n))
	
	ms, ls = gauss_elimination (ms, k, n)
	
	file2 = open (name2, "w")
	file2.write (str(n) + ' ' + str(k))
	for s in np.char.mod('%s', ms):
		file2.write ('\n' + ''.join (s))
	file2.write ('\n')
	file2.write (' '.join (str(e) for e in ls))
	file2.close ()
				
if __name__ == "__main__":
	standartise (sys.argv[1], sys.argv[2])