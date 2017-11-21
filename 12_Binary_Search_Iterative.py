# Binary Search

def binarySearch(arr, x):
	left = 0
	right = len(arr) - 1

	while left <= right:
		mid = int((left + right) / 2)
		
		if x == arr[mid]:
			return True
		elif x < arr[mid]:
			right = mid - 1
		else:
			left = mid + 1 

	return False


def main():

	my_list = [1,2,3,4,5,6,7,8,9,12,23,34,45,56,67,78,89,99]
	
	for i in range(100):
		if binarySearch(my_list, i):
			print "%d is in the list!" % i
		else:
			print "%d is NOT in the list :(" % i




if __name__ == '__main__':
	main()