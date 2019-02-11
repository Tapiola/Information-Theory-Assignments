import sys
import sympy as sp
a, x = sp.symbols ('a,x')

def minimal (name1, name2, name3):
	file1 = open (name1, "r")
	read_ls = file1.readlines ()
	file1.close ()

	p = int (read_ls[0].split()[0])
	n = int (read_ls[1].split()[0])

	pol_ls = read_ls[2].split()
	fl = sum ([int (pol_ls[i])*a**i for i in range (n + 1)])

	file2 = open (name2, "r")
	read_ls = file2.readlines ()
	file2.close ()

	deg = int (read_ls[0].split()[0])

	r_first = sp.rem (a**deg, fl, a, modulus=p)
	r_last = r_first
	squ = sp.poly (x - r_first, x, a, modulus=p)
	while True:
		deg *= p
		r = sp.rem (r_last**p, fl, a, modulus=p)
		r_last = r
		if r == r_first:
			break
		squ = sp.poly (squ * sp.poly (x - r, x, a, modulus=p), modulus=p)

	res = sp.poly (squ, x).all_coeffs ()

	file3 = open (name3, "w")
	file3.write (str (p) + '\n')
	file3.write (str (len (res) - 1) + '\n')
	for i in reversed (range (len (res))):
		file3.write (str (int (sp.rem (res[i], fl, a, modulus=p)) % p))
		if i == 0: file3.write ('\n')
		else: file3.write (' ')

		

	file3.close ()

if __name__ == "__main__":
	minimal (sys.argv[1], sys.argv[2], sys.argv[3])