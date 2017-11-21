class BinarySearch{
	
	public static boolean binarySearch(int arr[], int x){
		return binarySearch(arr, x, 0, arr.length - 1);
	}
	
	public static boolean binarySearch(int arr[], int x, int left, int right){
		// If the number is not it the array
		if(left > right){
			return false;
		}

		int mid = (left + right) / 2;

		if(x == arr[mid]){
			return true;
		}else if(x < arr[mid]){
			return binarySearch(arr, x, left, mid - 1);
		}else{
			return binarySearch(arr, x, mid + 1, right);
		}
	}
	
	public static void main(String[] args) {
		int[] list = {0,2,3,6,7,23,36,56,67,78,78,99};
		
		for(int i = 0; i < 60; i++){

		    int search = i;
			if(binarySearch(list, search)){
				System.out.printf("%d is in the list.\n", search);
			}else{
				System.out.printf("%d is in NOT the list.\n", search);
			}		
		}
	}
}