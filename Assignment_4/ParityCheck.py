import sys
import sympy as sp
x = sp.symbols ('x')

def parity (name1, name2):
	file1 = open (name1, "r")
	read_ls = file1.readlines()
	file1.close ()

	p = int (read_ls[0].split()[0])
	n = int (read_ls[1].split()[0])

	new_ls = read_ls[2].split()
	gen = sum ([int (new_ls[i])*x**i for i in range (n)])
	num = x**n - 1 

	q, r = sp.div (num, gen, x, modulus=p)

	file2 = open (name2, "w")
	if not r == 0:
		file2.write ('NO\n')
		file2.close()
		return

	file2.write ('YES\n')

	h = sp.poly (q).all_coeffs()
	for i in reversed (range (len (h))):
		if not i == len (h) - 1: file2.write (' ')
		file2.write (str (h[i] % p))

	for i in (range (n - sp.degree (q) - 1)):
		file2.write (' 0')

	file2.write ('\n')
	file2.close()


if __name__ == "__main__":
	parity (sys.argv[1], sys.argv[2])