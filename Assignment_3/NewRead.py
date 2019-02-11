import sys
import binascii

#reads byte array from file
def file_reader (name):
	file = open (name, "rb")
	read_bytes = file.read ()
	file.close ()
	return read_bytes

	
#writes binary string into file
def bytes_to_binary (read_bytes):
	tmp = byte_unfiller (read_bytes[-1])
	read_bytes = read_bytes[:-1]
	
	bin_str = ''
	for i in range (len (read_bytes)):
		bin_str += format(read_bytes[i], '08b')
	if not tmp == None:
		bin_str += tmp
	return bin_str


def byte_unfiller (byte):
	shift = 8 - format(byte, '08b').rfind('1')
	if shift == 8: return None
	byte = byte >> shift
	return format(byte, '0b').zfill(8 - shift)


def byte_writer (name, byte_str):
	read_bytes = []
	beg = 0
	while True:
		read_bytes.append (byte_str[beg:beg+8])
		beg += 8
		if beg >= len (byte_str):
			break
	
	file = open (name, "wb")
	for byte in read_bytes:
		if not byte == '':
			file.write (binascii.unhexlify ('%02x' % int(byte, 2)))
