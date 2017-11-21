class NumberOfOnes{
	public static void main(String[] args) {
		int[] test_case = {3, 4, 5, 6, 12, 43, 123, 156, 1123};
		int sum, temp;
		
		for(int i: test_case){
			temp = i;
			sum = 0;
			while(temp > 0){
				sum += temp & 1;
				temp >>= 1;
			}
			
			System.out.printf("Ones in %s: %d\n", Integer.toString(i, 2), sum);
		}
	}
}