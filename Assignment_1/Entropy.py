import sys
import math

def entropies (name1, name2):
	file1 = open (name1, "r")
	file2 = open (name2, "w")

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

	entropy = [0, 0, 0]
	for i, sm in enumerate(probs):
		probs[sm] /= len(to_find)
		if probs[sm] > 0:
			if i <= 33:
				entropy[0] -= probs[sm] * math.log2 (probs[sm])
			if i > 33:
				entropy[1] -= probs[sm] * math.log2 (probs[sm])
	entropy[2] = entropy[1] - entropy[0]

	for i in range(3):
		file2.write (format(entropy[i], ".7f"))
		if not i == 2:
			file2.write ("\n")

entropies (sys.argv[1], sys.argv[2])