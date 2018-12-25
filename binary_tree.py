class Node:
	def __init__(self, v, compare_=lambda x, y : x<y):
		self.value = v
		self.right = None
		self.left = None
		self.compare = compare_

	def add(self, v):
		if(self.compare(self.value, v)):
			if(self.right == None):
				self.right = Node(v)
			else:
				self.right.add(v)
		else:
			if(self.left == None):
				self.left = Node(v)
			else:
				self.left.add(v)

	def toList(self):
		r = []
		if self.left != None:
			r += self.left.toList()
		r.append(self.value)
		if self.right != None:
			r += self.right.toList()
		return r


class BinaryTree:
	def __init__(self, l=[], compare_=lambda x, y : x<y):
		self.root = None
		for e in l:
			self.add(e)

	def add(self, a):
		if self.root == None:
			self.root = Node(a)
		else:
			self.root.add(a)

	def toList(self):
		return self.root.toList()

	def __str__(self):
		return str(self.toList())

if __name__ == '__main__':
	bt = BinaryTree()
	bt.add(2)
	bt.add(5)
	bt.add(6)
	bt.add(1)
	print(bt)