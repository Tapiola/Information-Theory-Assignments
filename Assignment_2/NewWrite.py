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
	string = ""
	for i in range (len (read_bytes)):
		string += format(read_bytes[i], '08b')
	return string


def byte_filler (read_bytes):
	if (len(read_bytes[-1]) < 8):
		read_bytes[-1] += '1'
		while (len(read_bytes[-1]) < 8):
			read_bytes[-1] += '0'
	else:
		read_bytes.append ('10000000')


def byte_writer (name, byte_str):
	read_bytes = []
	beg = 0
	while True:
		read_bytes.append (byte_str[beg:beg+8])
		beg += 8
		if beg >= len (byte_str):
			break
	byte_filler (read_bytes)

	file = open (name, "wb")
	for byte in read_bytes:
		if not byte == '':
			file.write (binascii.unhexlify ('%02x' % int(byte, 2)))
