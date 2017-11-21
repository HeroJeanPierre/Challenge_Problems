 #      5
 #    /   \
 #   2     7
 #  / \   / \
 # 1   3 6   8

 class Node:
 	def __init__(self, data=None, left=None, right=None):
 		self.data=data
		self.left=left
 		self.right=right

 class BST:
 	def __init__(self):
 		self.root=Node()

 	def insert(self, data):
 		_insert(self.root, data)

 	def _insert(self, current_node, data):

 		if(current_node ==)
