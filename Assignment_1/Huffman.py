import sys
import math

class Node:

	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

	def code_tree (self, codes, c):
		codes [self.data[1]] = c
		if self.left:
			self.left.code_tree (codes, c + '1')
		if self.right:
			self.right.code_tree (codes, c + '0')		

def build (nodes):
	if len (nodes) == 1:
		return 
	elif len (nodes) >= 2:
		n0 = min (nodes, key = lambda x: x.data[0])
		del nodes[nodes.index(n0)]
		n1 = min (nodes, key = lambda x: x.data[0])
		del nodes[nodes.index(n1)]

		parent = Node ((n0.data[0] + n1.data[0], 0))
		parent.left = n0
		parent.right = n1

		nodes.append(parent)
		build (nodes)

		return

def huffman (name1, name2):
	file1 = open (name1, "r")
	file2 = open (name2, "w")
	probs = list(map (float, file1.read().split()))
	nodes = []
	codes = []
	codes.append('')
	for i in range(1, len(probs)):
		nodes.append (Node ((probs[i], i)))
		codes.append('')

	build (nodes)
	Node.code_tree (nodes[0], codes, '')

	for i in range(1, len(codes)):
		if not i == 1:
			file2.write("\n")
		file2.write(codes[i])

huffman (sys.argv[1], sys.argv[2])