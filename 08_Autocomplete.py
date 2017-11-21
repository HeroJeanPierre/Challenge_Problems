# Build an autocomplete function

class node:
	def __init__(self):
		self.prefix=""
		self.children={}
		self.isWord=False

class trie:

	# Create an empty to reprisent the first node
	def __init__(self):
		self.root=node()

	# Insert a word into the trie
	def insert(self, word):
		current_node = self.root
		temp = ""
		for i in word:
			temp += i

			if i not in current_node.children:
				current_node.children[i] = node()
				current_node.children[i].prefix = temp

			# Iterate the node to the next node in the trie
			current_node = current_node.children[i]

		# We will be at the end of the word now
		current_node.isWord = True

	def display(self):
		self._display(self.root)

	def _display(self, current_node):

		if len(current_node.children) == 0:
			return

		for i in current_node.children:
			print i
			self._display(current_node.children[i])

	def search(self, word):
		current_node = self.root

		for i in word:
			# print "beep"
			if i not in current_node.children:
				print "ERROR: Not in dictionary."
				return 
			current_node = current_node.children[i]

		return current_node

	def getWordsForAutocomplete(self, prefix):
		# This is what is going to hold all of the found words
		results = []

		current_node = self.root


		for i in prefix:
			if i in current_node.children:
				current_node = current_node.children[i]
			else:
				# If the prefix is not in the trie
				return results

		self.findAllChildWords(current_node, results)
		return resultskkkkk

	def findAllChildWords(self, current_node, results):
		if current_node.isWord:
			results.append(current_node.prefix)

		for i in current_node.children:
			self.findAllChildWords(current_node.children[i], results  )



def fill_dict(file):

	trie_dict = trie()
	f = open(file)

	for i in f.read().split("\n"):
		trie_dict.insert(i)

	return trie_dict
	f.close()

def main():
	# # Load dictionary
	trie_dict = fill_dict("dictionary/dict.txt")
	

	prefix = "work"


	while True:
		prefix = raw_input("What prefix would you like to check: ")
		
		for i in trie_dict.getWordsForAutocomplete(prefix):
			print i

	
 


if __name__ == '__main__':
	main()
