# Create a linked list in python


class node:
	def __init__(self, data=None):
		self.data=data
		self.next=None

class linkedList:
	def __init__(self):
		self.head=node()
	
	 

	def erase(self, index):
		if(index >= self.size()):
			print("ERROR: Index to large to append.")
			return None

		current_node = self.head
		current_index = 0

		while index != current_index:
			current_node = current_node.next
			current_index += 1

		current_node.next = current_node.next.next

	def get(self, index):
		if(index >= self.size()):
			print("ERROR: Index to large to append.")
			return4

		current_node = self.head
		current_index = 0

		while index != current_index:
			current_node = current_node.next
			current_index += 1

		return current_node.next.data
	
	def size(self):
		current_node = self.head
		length = 0

		while current_node.next != None:
			current_node = current_node.next
			length+=1
		return length

	def display(self):
		current_node = self.head
		index = 0

		while current_node.next != None:
			current_node = current_node.next
			print "Node", index, "is:", current_node.data
			index+=1

my_list = linkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.display()
print "Size of list:", my_list.size()
my_list.erase(3)
my_list.display()

print "The 2 indice of the list is", my_list.get(3)
