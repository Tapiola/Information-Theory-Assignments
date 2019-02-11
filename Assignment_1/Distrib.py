import sys

def distributions (name1, name2):
	file1 = open (name1, "r")
	st = " აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ"
	probs = {}
	for c in st: probs[c] = 0;
	for c in st:
		for x in st: 
			probs[c+x] = 0;

	to_find = file1.read ()
	probs[to_find[0]] += 1
	probs[' ' + to_find[0]] += 1
	for i in range (1, len(to_find)):
		probs[to_find[i-1] + to_find[i]] += 1
		probs[to_find[i]] += 1

	file2 = open (name2, "w")
	for i, sm in enumerate(probs):
		if not i == 0 and not i == 34:
			file2.write (" ")
		if i == 34:
			file2.write ("\n")
		file2.write (format(probs[sm]/len(to_find), ".7f"))
	
distributions (sys.argv[1], sys.argv[2])