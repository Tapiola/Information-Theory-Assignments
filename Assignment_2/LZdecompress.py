import sys
import math
from  NewRead import file_reader, byte_writer, bytes_to_binary
from Elias import de_elias


def lempel_ziv (data, lz_dic, N):
	res = ''
	beg = 0

	for i in range (N):
		if beg >= len (data): break
		siz = math.ceil (math.log2 (len (lz_dic)))
		ind_str = data[beg:beg+siz]
		if len (ind_str) < siz:
			ind_str += ''.join (['0' for j in range (siz-len(ind_str))])
		ind = int (ind_str, 2)

		res += lz_dic[ind]

		lz_dic.append (lz_dic[ind] + '1')
		lz_dic[ind] = lz_dic[ind] + '0'

		beg += siz	
	return res[:N*8]


def decompress (name1, name2):

	read_bytes = file_reader (name1)

	data = bytes_to_binary (read_bytes)
	N, offset = de_elias (data)

	lz_dic = ['0', '1']

	bin_str = lempel_ziv (data[offset:], lz_dic, N)
	byte_writer (name2, bin_str)



decompress (sys.argv[1], sys.argv[2])