import sys

#reads byte array from file
def file_reader (name):
	file = open (name, "rb")
	read_bytes = file.read ()
	return read_bytes

#writes binary string into file
def byte_writer (name, read_bytes):
	file = open (name, "w")
	for c in read_bytes:
		file.write (format(c, '08b'))

read_bytes = file_reader (sys.argv[1])
byte_writer (sys.argv[2], read_bytes)
