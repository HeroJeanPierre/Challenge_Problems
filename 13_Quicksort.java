import java.util.Random;


class Quicksort{

	public static int[] randomArr(int size, int min, int max){
		Random rand = new Random();
		int[] arr = new int[size];

		for(int i = 0; i < size; i++){
			arr[i] = rand.nextInt(max - min + 1) + min;
		}

		return arr;
	}

	public static void quicksort(int[] arr){
		quicksort(arr, 0, arr.length - 1);
	}

	public static void quicksort(int[] arr, int left, int right){
		if(left < right){
			int pIndex = partition(arr, left, right);
			quicksort(arr, left, pIndex - 1);
			quicksort(arr, pIndex + 1, right);
		}
	}

	public static int partition(int[] arr, int start, int end){

		int pivot = arr[end];
		int pIndex = start;

		// Doesn't <= end because the last index is
		// being used for the pivot
		for(int i = start; i < end; i++){
			if(arr[i] <= pivot){
				swap(arr, i, pIndex);
				pIndex++;
			}
		}

		swap(arr, end, pIndex);
		return pIndex;
	}

	public static void swap(int[] arr, int i, int j){
		int temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
	}

	public static void main(String[] args) {
		int[] unsorted_array = randomArr(1000000, 0, 100);
		// int[] unsorted_array = {3,2,5,1,4};

		// Print array BEFORE sort
		// for(int i : unsorted_array) System.out.printf("%d ", i);
		// System.out.println(); // Newline

		quicksort(unsorted_array);

		// Print array AFTER sort`
		// for(int i : unsorted_array) System.out.printf("%d ", i);
		// System.out.println(); // Newline			
	}
}