class node:
	def __init__(self, data=None):
		self.data = data
		self.next = None

class queue:
	def __init__(self):
		self.head = node()
		self.tail = node()


	def isEmpty(self):
		return self.head == None or self.head.data == None


	def peek(self):
		if self.isEmpty():
			print "Error: Queue is empty."
			return

		return self.tail.data

	def enqueue(self, data):
		new_node = node(data)

		if self.tail.data != None:
			self.tail.next = new_node

		self.tail = new_node

		if self.isEmpty():
			self.head = new_node


	def dequeue(self):
		if self.isEmpty():
			self.tail = node()
			print "Error: Qeueu is Empty."
			return

		data = self.head.data
		self.head = self.head.next


		return data



def main():
	queue_1 = queue()


	print "----------------"
	print "Queue Simulator"
	print "----------------"

	while True:
		print "\nWhat would you like to do?"
		print "1. Peek"
		print "2. Enque"
		print "3. Deque"
		print ""

		answer = raw_input("Answer: ").split()
		# print answer[0]
		if int(answer[0]) == 1:
			print queue_1.peek()
		elif int(answer[0]) == 2:
			print "Enque:", answer[1]
			queue_1.enqueue(int(answer[1]))
		elif int(answer[0]) == 3:
			print queue_1.dequeue()	
		else:
			print "Invalid input:", answer[0] 
	pass



if __name__ == '__main__':
	main()