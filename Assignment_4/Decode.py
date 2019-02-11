import sys
import sympy as sp
x = sp.symbols ('x')

def decode (name1, name2, name3):
	file1 = open (name1, "r")
	read_ls = file1.readlines()
	file1.close ()

	p = int (read_ls[0].split()[0])
	n = int (read_ls[1].split()[0])

	pol_ls = read_ls[2].split()
	gen = sum ([int (pol_ls[i])*x**i for i in range (n)])

	file2 = open (name2, "r")
	read_ls = file2.readlines()
	file2.close ()

	N = int (read_ls[0].split()[0])

	c_ls = read_ls[1].split()
	msg_size = n - sp.degree (gen)
	msg_count = int (N/n)

	file3 = open (name3, "w")
	file3.write (str (msg_count * msg_size) + '\n')

	for i in range (n, N + 1, n):
		code = sum ([int (c_ls[j])*x**(j % n) for j in range (i - n, i)])
		msg = sp.poly (sp.div (code, gen, x, modulus=p)[0])
		m = msg.all_coeffs ()
		for j in reversed (range (len (m))):
			if not (i == n and j == len(m) - 1): file3.write (' ')
			file3.write (str (m[j] % p))

		for j in (range (msg_size - sp.degree (msg) - 1)):
			file3.write (' 0')

	file3.write ('\n')		
	file3.close ()


if __name__ == "__main__":
	decode (sys.argv[1], sys.argv[2], sys.argv[3])