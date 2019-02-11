import sys
from  CompleteWrite import file_reader, byte_writer

def compress (code_file, name1, name2):
	code_file = open (code_file, "r")
	file1 = open (name1, "r")
	file2 = open (name2, "w")
	lang = " აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ"
	code = code_file.read().split()
	code_file.close()
	encoding = dict (zip (lang, code))
	
	text = file1.read()
	file1.close ()
	for c in text:
		file2.write (encoding[c])
	file2.close ()

	read_bytes = file_reader(name2)
	byte_writer (name2, read_bytes)

compress (sys.argv[1], sys.argv[2], sys.argv[3])