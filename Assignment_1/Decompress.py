import sys
from  CompleteRead import file_reader, byte_writer

def decompress (code_file, name1, name2):
	code_file = open (code_file, "r")
	
	lang = " აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ"
	code = code_file.read().split()
	code_file.close()
	encoding = dict (zip (code, lang))

	read_bytes = file_reader (name1)
	encoded = byte_writer (read_bytes)

	file2 = open (name2, "w")
	bit_count, bit_curr = (0, '')
	for c in encoded:
		bit_count += 1
		bit_curr += c
		if bit_curr in encoding:
			file2. write (encoding[bit_curr])
			bit_count = 0
			bit_curr = ''
	file2.close ()

decompress (sys.argv[1], sys.argv[2], sys.argv[3])