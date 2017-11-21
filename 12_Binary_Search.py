# Binary Search

def binarySearch(arr, x):
	return _binarySearch(arr, x, 0, len(arr) - 1)

def _binarySearch(arr, x, left, right):
	if left > right:
		return False

	mid = int((left + right) / 2)

	if x == arr[mid]:
		return True
	elif x < arr[mid]:
		return _binarySearch(arr, x, left, mid - 1)
	elif x > arr[mid]:
		return _binarySearch(arr, x, mid + 1, right)

def main():
	my_list = [1,2,3,4,5,6,7,8,9,12,23,34,45,56,67,78,89,99]
	
	for i in range(20):
		if binarySearch(my_list, i):
			print "%d is in the list!" % i
		else:
			print "%d is NOT in the list :(" % i




if __name__ == '__main__':
	main()