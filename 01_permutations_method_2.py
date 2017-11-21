def permutations(string):
	_permutations("", string)

def _permutations(result, string):
	if len(string) == 0:
		print result

	for i in range(len(string)):
		_permutations(result + string[i], string[0:i] + string[i+1:])


permutations("abc")