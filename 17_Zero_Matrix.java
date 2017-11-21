class ZeroMatrix{

	public static void printArray(boolean[][] arr){
		// Print the array
		for(int i = 0; i < arr.length; i++){
			for(int j = 0; j < arr[0].length; j++){
				System.out.print(arr[i][j] + "\t");
			}
			System.out.println();
		}
	}

	public static void main(String[] args){
		boolean[][] test_case = {{false, false, false, false, false, false, false}
								,{true, false, false, false, false, false, false}
								,{false, false, false, false, false, false, false}
								,{false, false, false, false, false, false, false}
								,{true, false, false, false, false, false, false}
								,{false, false, false, false, false, false, false}
								,{false, false, false, false, false, false, false}
								,{false, false, false, false, false, false, false}};

		// Are the first row and column zero?
		boolean rowZ = false;
		boolean colZ = false;

		printArray(test_case);
		System.out.println("\n------------------------------------------------------\n");

		// First pass
		for(int i = 0; i < test_case.length; i++){
			for(int j = 0; j < test_case[0].length; j++){
				if(test_case[i][j]){
					test_case[0][j] = true;
					test_case[i][0] = true;

					if(i == 0) rowZ = true;
					if(j == 0) colZ = true;
				}

			}
		}

		// Second pass
		for(int i = 1; i < test_case.length; i++){
			for(int j = 1; j < test_case[0].length; j++){
				if(test_case[0][j]){
					test_case[i][j] = true;
				}

				if(test_case[i][0]){
					test_case[i][j] = true;
				}
			}
		}

		// Set the first and second rows
		if (rowZ){
			for(int i = 0; i < test_case[0].length; i++){
				test_case[0][i] = true;
			}
		}

		if(colZ){
			for(int i = 0; i < test_case.length; i++){
				test_case[i][0] = true;
			}
		}

		printArray(test_case);
	}
}