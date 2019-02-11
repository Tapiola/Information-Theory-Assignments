import sys
import math
from  NewWrite import file_reader, byte_writer, bytes_to_binary
from Elias import elias


def index_to_byte (ind, N):
	return format (ind, '0b').zfill (math.ceil (math.log2 (N)))


def lempel_ziv (bin_str, lz_dic):
	res = ''
	beg = 0
	for i in range (1, len (bin_str) + 1):
		if bin_str[beg:i-1] in lz_dic and not bin_str[beg:i] in lz_dic:
			seq = bin_str[beg:i-1]
			ind = lz_dic[seq]
			ind_b = index_to_byte (ind, len (lz_dic))
			res += ind_b

			lz_dic[seq + '1'] = len (lz_dic)
			lz_dic[seq + '0'] = ind

			del lz_dic[seq]

			beg = i - 1

	bin_str += '000000000000000'
	for i in range (beg, len (bin_str) + 1):
		if bin_str[beg:i] in lz_dic:
			seq = bin_str[beg:i]
			ind = lz_dic[seq]
			ind_b = index_to_byte (ind, len (lz_dic))
			res += ind_b
			break			
	return res


def compress (name1, name2):

	read_bytes = file_reader (name1)
	N = len (read_bytes)
	bin_str = elias (N)

	data = bytes_to_binary (read_bytes)

	lz_dic = {'0':0, '1':1}
	bin_str += lempel_ziv (data, lz_dic)

	byte_writer (name2, bin_str)

	

compress (sys.argv[1], sys.argv[2])

