import sys

#reads byte array from file
def file_reader (name):
	file = open (name, "rb")
	read_bytes = file.read ()
	file.close ()
	return read_bytes

#resets non 8-aligned bytes to original size
def byte_unfiller (byte):
	shift = 8 - format(byte, '08b').rfind('1')
	if shift == 8: return ""
	byte = byte >> shift
	return format(byte, '0b').zfill(8 - shift)
	
#writes binary string into file
def byte_writer (read_bytes):
	string = ""
	for i in range (len (read_bytes) - 1):
		string += format(read_bytes[i], '08b')
	string += byte_unfiller (read_bytes[-1])
	return string