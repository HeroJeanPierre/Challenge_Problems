#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*This will give an optimal solution most of the time
  However, it doesn't ALL of the time.
  */




/*The method is to just iterate throught he highest coin value
  checkin if it is smaller than the current cent value, and if 
  if is, add 1 to the total coin coint.
  */

int least_coins(int coins[], int coin_legnth, int cents){

	int number_of_coins = 0;
	printf("Number of types of coins: %d\n", coin_legnth);

	for(int i = coin_legnth - 1; i >= 0; i--){
		while(cents >= coins[i]){
			cents -= coins[i];
			number_of_coins++;
			printf("Cents: %d\n", cents);
		}
	}

	return number_of_coins;
}

int main(int argc, char *argv[]){

	if(argc >= 3){
		printf("Too many arguments!\n");
		exit(1);
	}else if(argc < 2){
		printf("Pass a cent amount!\n");
		exit(0);
	}

	printf("Number of args = %d\n", argc);

	int coin_types[4] = {1, 5, 10, 25};

	int cents = atoi(argv[1]);
	int coins = least_coins(coin_types, sizeof(coin_types)/sizeof(coin_types[0]), cents);

	printf("The least number of coins to produce change for %d cents is: %d coins\n", cents, coins);

	return 0;
}