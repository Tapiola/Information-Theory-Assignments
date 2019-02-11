import sys

class Node:

	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

def traverse (node, curr_d, lens, codes):
	if curr_d == lens[0][0]:
		codes [lens[0][1]-1] = node.data
		del lens[0]
		return 0
	else:
		if len (lens) > 0:
			node.left = Node (node.data + '0')
			traverse (node.left, curr_d + 1, lens, codes) == 0
		if len (lens) > 0:
			node.right = Node (node.data + '1')
			traverse (node.right, curr_d + 1, lens, codes) == 0
		return -1

def prefixless (name1, name2):
	file1 = open (name1, "r")
	file2 = open (name2, "w")
	lens = list(map (int, file1.read().split()))
	new_lens = []
	codes = []
	summy = 0
	for i in range(1, len(lens)):
		summy += (1/2)**lens[i]
		new_lens.append ((lens[i], i))
		codes.append('')
	if (summy > 1): return
	
	new_lens = sorted (new_lens)

	node = Node ('')
	curr_d = 0
	length = 3
	traverse (node, curr_d, new_lens, codes)

	for i in range(len(codes)):
		if not i == 0:
			file2.write("\n")
		file2.write(codes[i])

prefixless (sys.argv[1], sys.argv[2])