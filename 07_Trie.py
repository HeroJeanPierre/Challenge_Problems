# Tries are fantastic for storing dictionaries, they take up
# less space than a hash table.

class node:
	def __init__(self, character=None):
		self.children = {} # This is a map {character: node*}
		self.endOfWord=False

class trie:
	def __init__(self):
		self.root = node()

	def insert_iterative(self, word):
		# set current nodd to the top of the tree
		current_node = self.root
		# hello
		# Let's iterate through the word, char by char
		for i in word:

			# if the current node doesn't have the
			# char we are looking for, we will create
			# a new child.
			if i not in current_node.children:
				# Create that child at character i
				current_node.children[i] = node()
			# Step into that new character
			current_node = current_node.children[i]
			# !!!This could be a place to dynamically program

		# It is now at the last char, this word is complete
		current_node.endOfWord = True


	def recursive_insert(self, word):
		self._recursive_insert(self.root, word, 0)

	def _recursive_insert(self, current_node, word, word_index):
		if word_index == len(word):
			current_node.endOfWord = True
			return

		# if the character is not in the children nodes of the 
		# current node, create a new node
		if(word[word_index] not in current_node.children):
			current_node.children[word[word_index]] = node()
			self._recursive_insert(current_node.children[word[word_index]], word, word_index+1)
			
		# If it IS in the children node.
		else:
			self._recursive_insert(current_node.children[word[word_index]], word, word_index+1)
	
	def display(self):
		self._display(self.root);

	def _display(self, current_node):
		# Base Case
		if current_node.endOfWord:
			return

		for i in current_node.children:
			print i
			self._display(current_node.children[i])
    # TODO:
	def search_iterative(self, word):
		current_node = self.root

		for i in word:
			if i in current_node.children:
				current_node = current_node.children[i]
			else:
				return False

		return True;

	def search_recursive(self, word):
		return self._search_recursive(self.root, word, 0)

	def _search_recursive(self, current_node, word, word_index):
		if word_index == len(word):
			return True

		if  word[word_index] in current_node.children:
			return self._search_recursive(current_node.children[word[word_index]], word, word_index + 1)
		else:
			return False

	def delete(self, word):
		self._delete(self.root, word, 0)

	def _delete(self, current_node, word, word_index):

		if word_index == len(word):
			# Only delete the node if the it is NOT the end of a word
			if not current_node.endOfWord: #This means the word wasn't in the trie to start
				return False

			current_node.endOfWord = False

			# if there are no more children, feel free to remove this entire word
			return len(current_node.children) == 0

		# If the word is not in the trie...
		if word[word_index] not in current_node.children:
			return False

		shouldDeleteCurrentNode = self._delete(current_node.children[word[word_index]], word, word_index + 1)

		if shouldDeleteCurrentNode:
			del current_node.children[word[word_index]]

			return len(current_node.children) == 0

		return False

	def size(self):
		return self._size(self.root, 0)

	def _size(self, current_node, current_size):
		if len(current_node.children) == 0:
			return current_size
		sum = 0;
		for i in current_node.children:
			sum += self._size(current_node.children[i], current_size + 1)

		return sum

	def depth(self):
		return self._depth(self.root, 0)

	def _depth(self, current_node, current_depth):
		if len(current_node.children) == 0:
			return current_depth

		temp = []
		for i in current_node.children:
			temp.append(self._depth(current_node.children[i], current_depth + 1))

		return max(temp)

	def average_depth(self):
		return self._average_depth(self.root, 0)

def main():

	f = open("dictionary/dict.txt")
	first_line = f.read().split("\n")

	first_try = trie()
	for i in first_line:
		first_try.insert_iterative(i)

	f.close()

	print "Size:", first_try.size()
	print "Max Depth:", first_try.depth()

	# first_try.display()
	# first_try.delete("56")
	# print "\n"
	# first_try.display()
	
if __name__ == '__main__':
	main()


