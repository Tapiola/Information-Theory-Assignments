import sys
import binascii

#reads binary string list from file
def file_reader (name):
	file = open (name, "r")
	read_bytes = []
	byte = file.read (8)
	while byte:
		read_bytes.append (byte)
		byte = file.read (8)
	return read_bytes

#writes hex bytes into file
def byte_writer (name, read_bytes):
	file = open (name, "wb")
	for byte in read_bytes:
		file.write (binascii.unhexlify ('%02x' % int(byte, 2)))

read_bytes = file_reader (sys.argv[1])
byte_writer (sys.argv[2], read_bytes)