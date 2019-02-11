import sys
import sympy as sp
a, x = sp.symbols ('a,x')



def minpoly (deg, p, fl):
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
	cf = sp.poly (squ, x).all_coeffs ()
	cf2 = [sp.rem (e, fl, a, modulus=p) for e in cf]
	n = len (cf2)
	fl = sum ([int (cf2[i] % p)*a**(n-i-1) for i in range (n)])

	return sp.poly (fl, a, modulus=p)


def bch (name1, name2, name3):
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

	dist = int (read_ls[0].split()[0])

	discovered = []
	squ = sp.poly (1, a, modulus=p)

	for i in range (1, dist):
		s = minpoly (i, p, fl)
		if s in discovered:
			continue
		discovered.append (s)
		squ = sp.poly (squ * sp.poly (s, a, modulus=p), modulus=p)

	N = p**n - 1
	g = squ.all_coeffs ()

	file3 = open (name3, "w")
	file3.write (str (p) + '\n')
	file3.write (str (N) + '\n')
	for i in reversed (range (len (g))):
		if not i == len (g) - 1: file3.write (' ')
		file3.write (str (g[i] % p))
	for i in (range (N - len (g))):
		file3.write (' 0')

	file3.write ('\n')
	file3.close ()


if __name__ == "__main__":
	bch (sys.argv[1], sys.argv[2], sys.argv[3])