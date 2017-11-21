class Node:
	def __init__(self, data=None, next=None):
		self.data=data
		self.next=next


class LinkedList:
	def __init__(self):
		self.head=Node()

	def isEmpty(self):
		return self.head.data == None

	def add(self, data):
		current_node = self.head
		new_node = Node(data)

		if(self.isEmpty()):
			self.head = new_node
			print "Adding:", data

		else:
			# Get to the end of the list
			while current_node.next != None:
				current_node = current_node.next
			print "Adding:", data
			current_node.next = new_node

	def print_reverse_recursive(self):
		self._print_reverse_recursive(self.head)

	def _print_reverse_recursive(self, current_node):
		# print "Running"
		if current_node.next == None:
			print current_node.data
			return

		self._print_reverse_recursive(current_node.next)
		print current_node.data

	def print_reverse_iterative(self):
		current_node = self.head

		if isEmpty():
			print "Error: No elements in list"

		
		while current_node == None:
			previous_node = current_node
			next_node = current_node.next

			# Iterate node
			current_node = next_node

			# Change next to prev
			current_node.next = previous_node


		while current_node  






def fill_list():
	list = LinkedList()
	list.add(1)
	list.add(2)
	list.add(3)
	list.add(4)
	list.add(5)
	list.add(6)
	list.add(7)
	list.add(8)
	list.add(9)
	list.add(10)
	list.add(11)
	list.add(12)
	list.add(13)
	list.add(14)
	list.add(15)
	return list


def main():
	list_1 = fill_list()
	list_1.print_reverse_recursive()



if __name__ == '__main__':
	main()