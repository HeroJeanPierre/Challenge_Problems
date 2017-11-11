# For example,"egg" and "add" are isomorphic, "foo" and "bar" are not.

# abccd -> 12334
# bhood -> 12334

# abbddbb -> 1223322

# aabccbbcc -> 112334455
# aabccddee -> 112334455

# Return the integer equivalent of the string
def intString(string):
	intString = ""
	unique_index = 0
	current_char = string[0]
	for i in string:
		intString += str(unique_index)
		if i != current_char:
			current_char = i
			unique_index+=1

	return intString

def isIsomorphic(string1, string2):
	if string1 == None or string1 == "":
		print("ERROR: String1 not valid.")
		return None

	# Well, if they are not the same length they are not Isomorphic
	if len(string1) != len(string1):
		return False

	# If there interger skeletons equal eachother they are isomorphic
	if intString(string1) == intString(string2):
		return True

	return False

a = "jjjdddnnnfffus"
b = "kkksssmmmdddne	"

print(isIsomorphic(a, b))