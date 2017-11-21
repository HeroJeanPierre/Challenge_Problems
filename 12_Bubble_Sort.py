from random import randint



def genList(size, min, max):
	result = []
	for _ in range(size): result.append(randint(min, max))
	return result

def bubbleSort(list),
	for i in range(len(list), -1, -1): 
		for j in range(1, i):
			if list[j-1] > list[j]:
				temp = list[j-1]
				list[j-1] = list[j] 
				list[j] = temp
	


def main():
	list = genList(8000,0, 1000 )
	# print list
	print "Sorting..."
	bubbleSort(list)
	# print list


if __name__ == "__main__":
	main()