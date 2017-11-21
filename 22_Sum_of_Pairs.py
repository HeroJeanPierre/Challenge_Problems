from random import randint

def pairsExist(arr, desired_sum):
	compliments ={}

	for i in arr:
		if desired_sum - i in compliments:
			print "%d + %d = %d" % (desired_sum - i, i, desired_sum)

		if i not in compliments:
			compliments[i] = desired_sum - i

def gen_arr(size, min, max):
	temp = []

	for i in range(size):
		temp.append(randint(min, max))

	return temp


def main():
	test_arr = [5, 4, 6, 7, 8, 3, 4, 2]
	desired_sum = 15


	for _ in range(10):
		# create arr
		arr = gen_arr(10, 1, 15)



		for __ in range(15):
			desired_sum = randint(6, 25)


			print "\n", arr
			print "Desired Sum:", desired_sum 
			pairsExist(arr, desired_sum)
		# print desired_sum, "can be made with pairs in", test_arr
		# else:
		# print desired_sum, "CANNOT be made with pairs in", test_arr

if __name__ == '__main__':
	main()