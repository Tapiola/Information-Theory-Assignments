import sys
import sympy as sp
x = sp.symbols ('x')

def encode (name1, name2, name3):
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

	m_ls = read_ls[1].split()
	msg_size = n - sp.degree (gen)
	msg_count = N/msg_size

	file3 = open (name3, "w")
	file3.write (str (msg_count * n) + '\n')

	for i in range (msg_size, N + 1, msg_size):
		msg = sum ([int (m_ls[j])*x**(j % msg_size) for j in range (i - msg_size,i)])
		code = sp.poly (sp.poly (msg) * sp.poly (gen), modulus=p) 
		c = code.all_coeffs()
		for j in reversed (range (len (c))):
			if not (i == msg_size and j == len(c) - 1): file3.write (' ')
			file3.write (str (c[j] % p))

		for j in (range (n - sp.degree (code) - 1)):
			file3.write (' 0')

	file3.write ('\n')		
	file3.close ()


if __name__ == "__main__":
	encode (sys.argv[1], sys.argv[2], sys.argv[3])