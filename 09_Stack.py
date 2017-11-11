# FILO

class node:
	def __init__(self, data=None):
		self.data = data
		self.next = None

class stack:
	# The top is where things will be popped and pushed
	def __init__(self):
		self.top = node()

	# Is this stack empty?
	def isEmpty(self):
		return self.top.data == None

	# Get a look at whats in the top
	def peek(self):
		if self.top.data == None:
			print "Stack Empty."
			return ""

		return self.top.data

	# Add elemet to the stack
	def push(self, data):
		new = node(data)
		new.next = self.top
		self.top = new

	def pop(self):
		if self.isEmpty():
			print "Error: Stack Empty."

		data = self.top.data
		self.top = self.top.next
		return data



def main():
	stack_1 = stack()


	print "----------------"
	print "Stack Simulator"
	print "----------------"

	while True:
		print "\nWhat would you like to do?"
		print "1. Peek"
		print "2. Push"
		print "3. Pop"
		print ""

		answer = raw_input("Answer: ").split()
		# print answer[0]
		if int(answer[0]) == 1:
			print stack_1.peek()
		elif int(answer[0]) == 2:
			print "Pushing to stack:", answer[1]
			stack_1.push(int(answer[1]))
		elif int(answer[0]) == 3:
			print stack_1.pop()	
		else:
			print "Invalid input:", answer[0] 


if __name__ == '__main__':
	main()