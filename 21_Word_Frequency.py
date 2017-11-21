class Node():
	def __init__(self, character=None):
		self.character = character
		self.number_of_occurrences = 0
		self.isWord = False
		self.children = {}

class Trie():
	def __init__(self):
		self.root = Node()

	def add(self, word):
		current_node = self.root

		# Iterate through the word char by char
		for i in word:

			# If it is not in the current node
			# children, create the new node
			if i not in current_node.children:
				current_node.children[i] = Node()

			# Enter into the next character
			current_node = current_node.children[i]

		current_node.isWord = True
		current_node.number_of_occurrences += 1

	def occurances(self, word):
		
		current_node = self.root

		for i in word:
			if i in current_node.children:
				current_node = current_node.children[i]
			else:
				return 0

		return current_node.number_of_occurrences




def main():
	t = Trie()
	t.add("abc")
	t.add("abc")
	t.add("abd")
	t.add("abd")
	t.add("abd")

	print t.occurances("abc")



if __name__ == '__main__':
	main()



