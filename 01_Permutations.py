# In this all the permutatation of a string will be generated recursively

# The first thing to do is to get the necessary information about the string
def getStringInfo(string):
	tempDict = {}

	# If there is a new character, intitiate it to 1 in the dictionary,
	# Otherwise, increment it by 1
	for i in string:
		if i not in tempDict:
			tempDict[i] = 1
		else:
			tempDict[i] += 1

	charArray = []
	charCount = []

	# Create 2 arrays fromt this dictionary
	# One array with the character value
	# The other with the number of times it occurs

	for i in tempDict:
		charArray.append(i)
		charCount.append(tempDict[i])

	return charArray, charCount

def printPerms(arr, count, index, result, length):
	# Copy array
	tempCount = count[:]
	tempCount[index] -= 1 

	# Base case, if result is the same size as the original string
	if len(result) == length:
		print(result)
		result = ""
		return

	# Find first non-zero character and add to result 
	for i in range(len(arr)):
		if(tempCount[i] >= 1):
			result += arr[i]
			index = i
			printPerms(arr, tempCount, index, result, length)
			result = result[:-1]
	while(True):
	print("")
	inputString = raw_input("Enter string you would like the permutations for: ")

	arr, count = getStringInfo(inputString)

	# Increment first index
	count[0] += 1 
	printPerms(arr,count, 0, "", len(inputString))