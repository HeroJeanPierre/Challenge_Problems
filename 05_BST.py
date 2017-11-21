# We are going to implement a binary search tree here 

class node:
	def __init__(self, key=None,name=None):
		self.key=key
		self.name=name
		self.right=None
		self.left=None

class BST:
	def __init__(self):
		self.root=None

	def insert(self, key, name):
		if self.root == None:
			self.root=node(key, name)
		else:
			self._insert(key, name,self.root)

	def _insert(self, key, name, current_node):

		if key < current_node.key: 
			if current_node.left == None:
				current_node.left = node(key, name)
			else:
				self._insert(key, name, current_node.left)
		elif key > current_node.key:
			if current_node.right == None:
				current_node.right = node(key, name)
			else:
				self._insert(key, name, current_node.right)
		else:
			print key, "already in tree!"

	def print_tree(self):
		if self.root != None:
			self._print_tree(self.root)
		else:
			print "This tree is empty."

	def _print_tree(self, current_node):
		if current_node != None:
			self._print_tree(current_node.left)
			print str(current_node.key) + ": " + current_node.name
			self._print_tree(current_node.right)

	def height(self):
		if(self.root != None):
			return self._height(self.root, 0)
		else:
			return 0

	def _height(self, current_node, current_height):
		if(current_node==None): return current_height

		left_height=self._height(current_node.left, current_height + 1)
		right_height=self._height(current_node.right, current_height + 1)
		return max(left_height, right_height)

	def search(self, key):
		if self.root != None:
			return self._search(self.root, key)
		else:
			return False

	def _search(self, current_node, key):
		if key == current_node.key: 
				 return current_node.name
		elif key < current_node.key and current_node.left != None:
			return self._search(current_node.left, key)
		elif key > current_node.key and current_node.right != None:
			return self._search(current_node.right, key)
		return False 




def fill_tree(tree, num_elems=100, max_int=100):
	from random import randint
	for _ in range(num_elems):
		cur_elem = randint(0,max_int)
		tree.insert(cur_elem)
	return treeii

tree = BST()
# tree = fill_tree(tree)
# tree.print_tree() 
# print "Max height is:", tree.height()
tree.insert(23, "Melissia")
tree.insert(63, "Wendie")
tree.insert(2, "Betty")
tree.insert(85, "Leota")
tree.insert(93, "Katheryn")
tree.insert(50, "Roxanna")
tree.insert(45, "Jimmy")
tree.insert(51, "Dannielle")
tree.insert(81, "Tamika")
tree.insert(87, "Ossie")
tree.insert(14, "Tony")
tree.insert(76, "Darrel")
tree.insert(36, "Vanda")
ltree.insert(49, "Claretta")
tree.insert(30, "Lyman")
# tree.print_tree() 


print tree.search(14)


