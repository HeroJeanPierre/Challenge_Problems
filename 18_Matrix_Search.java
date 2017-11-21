import java.util.Random;

class MatrixSearch{

	// time complexity = O(m + n) space complexity = O(1) 
	public static boolean inMatrix(int[][] arr, int n){
		if(arr.length == 0 || arr[0].length == 0) return false;

		int row = 0;
		int col = arr[0].length - 1;

		while(row < arr.length && col >= 0){
			if(n == arr[row][col]){
				return true;
			}else if(n > arr[row][col]){
				row++;
			}else if(n < arr[row][col]){
				col--;
			}
		}

		return false;
	}


	public static void main(String[] args){
		Random rand = new Random();
		int[][] test_case = {{1,  2,  3, 4,  5},
							 {6,  8,  10,12, 14},
							 {16, 18, 20,22, 24},
							 {26, 28, 30,32, 34}};

		for(int n = 0; n < 35; n++){
			if(inMatrix(test_case, n)){
				System.out.printf("%d is in Matrix!\n", n);
			}else
		}
	}
}