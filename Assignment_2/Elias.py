import sys
import math


def elias (N):
	res = ''
	N_len = math.ceil (math.log2 (N))
	res += ''.join (['0' for i in range (N_len-1)])
	res += format (N, '08b')
	return res

def de_elias (bin_str):
	count = 0
	while not bin_str[count] == '1':
		count += 1
	return int (bin_str[count:2*count+1], 2), 2*count+1