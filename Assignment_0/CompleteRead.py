import sys

#reads byte array from file
def file_reader (name):
	file = open (name, "rb")
	read_bytes = file.read ()
	return read_bytes

#resets non 8-aligned bytes to original size
def byte_unfiller (file, byte):
	shift = 8 - format(byte, '08b').rfind('1')
	if shift == 8: return
	byte = byte >> shift
	file.write (format(byte, '0b').zfill(8 - shift))
	
#writes binary string into file
def byte_writer (name, read_bytes):
	file = open (name, "w")
	for i in range (len (read_bytes) - 1):
		file.write (format(read_bytes[i], '08b'))
	byte_unfiller (file, read_bytes[-1])
	

read_bytes = file_reader (sys.argv[1])
byte_writer (sys.argv[2], read_bytes)