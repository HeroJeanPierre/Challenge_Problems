# Returns array of arrays
def getArrs(number_of_arrs, size):
	from random import randint
	array_holder = []

	for _ in range(number_of_arrs):
		temp = []

		for i in range(size):
			temp.append(randint(1, size))

		array_holder.append(temp)

	return array_holder;


# This will run in O(n) time, and O(n) space
def numberOfDups_FirstSolution(arr):
	temp = {}
	dups = []
	for i in arr:
		if i not in temp:
			temp[i] = 0
		elif i in temp and temp[i] == 0:
			dups.append(i)
			temp[i] += 1

	return dups


# O(n) time, O(1) space
def numbderOfDupsBest(arr):
	# Will contain dups
	temp = set()

	for i in range(len(arr)):
		if arr[abs(arr[i]) - 1] < 0:
			temp.add(abs(arr[i]))	

		arr[abs(arr[i]) - 1] *= -1

	for i in range(len(arr)):
		arr[i] = abs(arr[i])

	return temp


# 
def main():

	# Retruns x arrays of size y getArrs(x, y)
	arr = getArrs(15, 9);

	for i in arr:
		print "Dups in", i, "is", numbderOfDupsBest(i)


if __name__ == "__main__":
	main()