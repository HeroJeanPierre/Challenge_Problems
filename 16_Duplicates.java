import java.util.*;


class Duplicates{
	public static int[][] getArrays(int number_of_arrays, int size){
		int[][] temp = new int[number_of_arrays][size];
		Random rand = new Random();	
		for(int i = 0; i < number_of_arrays; i++){
			for(int j = 0; j < size; j++){
				temp[i][j] = rand.nextInt(size - 1) + 1;
			}
		}

		return temp;
	}

	public static Set<Integer> getDups(int arr[]){
		Set<Integer> dups = new HashSet<Integer>();

		for(int i = 0; i < arr.length; i++){

			if(arr[Math.abs(arr[i]) - 1] < 0){
				// System.out.printf("Adding %d, at int %d", Math.abs(arr[Math.abs(arr[i]) - 1]), i);
				dups.add(Math.abs(arr[i]));
			}
			arr[Math.abs(arr[i]) - 1] *= -1;
		}

		for(int i = 0; i < arr.length; i++){
			arr[i] = Math.abs(arr.length);
		}

		return dups;
	}

	public static void main(String[] args) {
		int[][] arrays = getArrays(10, 9);
		Set<Integer> current_dups = new HashSet<Integer>();

		for(int i = 0; i < arrays.length; i++){

			System.out.printf("[ ");

			for(int j = 0; j < arrays[i].length; j++){
				System.out.printf("%d ", arrays[i][j]);
			}

			System.out.printf("]");
			current_dups = getDups(arrays[i]);
			System.out.printf(" : [ ");

			for(int k: current_dups){
				System.out.printf("%d ", k);
			}

			System.out.printf("]\n");
			current_dups.clear();
		}
	}
}