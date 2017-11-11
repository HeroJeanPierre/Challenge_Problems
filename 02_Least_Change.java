class LeastChange{

	public int leastChange(int current_change, int[] coins){
		int[] cache = new int[current_change];
		for (int i = 1; i < cache.length; i++) cache[i] = -1;
		return leastChange(current_change, coins, cache); 
	}

	public int leastChange(int current_change, int[] coins, int[] cache){
		if(current_change == 0){
			return 0;
		}

		int min = current_change;
		for(int coin : coins){
			// If the number has been cached
			if(current_change - coin >= 0){
				int coin_count;
				if(cache[current_change - coin] >= 0){
					coin_count = cache[current_change - coin];
				}else{
					coin_count = leastChange(current_change - coin, coins, cache);
					cache[current_change - coin] = coin_count;
				}

				if(min > coin_count + 1) min = coin_count + 1;
			}
		}

		return min;
	}


	public static void main(String[] args){
		int[] coins = {25, 10, 5, 1};
		int change = 123456;

		LeastChange a = new LeastChange();
		int least = a.leastChange(change, coins);
		System.out.printf("Least change for %d is %d\n", change, least);
	}
}