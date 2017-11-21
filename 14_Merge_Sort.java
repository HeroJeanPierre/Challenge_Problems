import java.util.Random;


class MergeSort{

	public static int[] randomArr(int size, int min, int max){
		Random rand = new Random();
		int[] arr = new int[size];

		for(int i = 0; i < size; i++){
			arr[i] = rand.nextInt(max - min + 1) + min;
		}

		return arr;
	}
	
	public static void mergeSort(int[] arr){
		int len = arr.length;

		if(len < 2){
			return;
		}

		// Create the midpoint
		int mid = (len / 2);

		// Seperate the array into 2 values
		int[] left = new int[mid];
		int[] right = new int[len - mid];

		// Set the new arrays to there values
		for(int i = 0; i < mid; i++) left[i] = arr[i];
		for(int i = mid; i < len; i++) right[i - mid] = arr[i];
		mergeSort(left);
		mergeSort(right);
		merge(left, right, arr);
	}

	public static void merge(int[] left, int[] right, int[] arr){
		int lenL = left.length;
		int lenR = right.length;
		int lenA = arr.length;

		int i = 0; // iterator for left
		int j = 0; // iterator for right
		int k = 0; // iterator for array

		while(i < lenL && j < lenR){
			if(left[i] <= right[j]){
				arr[k] = left[i];
				i++;
			}else{
				arr[k] = right[j];
				j++;
			}			
			k++;
		}

		while(i < lenL){
			arr[k] = left[i];
			i++;
			k++;
		}

		while(j < lenR){
			arr[k] = right[j];
			j++;
			k++;
		}
	}

	public static void main(String[] args) {
		int[] unsorted_array = randomArr(100, 0, 100);

		// Print array BEFORE sort
		for(int i : unsorted_array) System.out.printf("%d ", i);
		System.out.println(); // Newline

		mergeSort(unsorted_array);

		// Print array AFTER sort
		for(int i : unsorted_array) System.out.printf("%d ", i);
		System.out.println(); // Newline
	}
}