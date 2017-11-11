# In this problem we will develope a solution to finding the least amount
# coins required to give change to a user





def least_change(current_change, coins, cache):
	if(current_change == 0):
		return 0

	min = current_change	

	for coin in coins:
		if (current_change - coin) >= 0:
			if current_change - coin in cache[0]:
				coin_number = cache[0][current_change - coin]
			else:
				coin_number = least_change(current_change - coin, coins, cache)
				cache[0][current_change - coin] = coin_number

			# Find the min of the change below, +1 to include this
			if min > coin_number + 1:
				min = coin_number + 1
				min = coin_number + 1

	return min

def _least_change(current_change, coins):
	if(current_change == 0):
		return 0

	min = current_change	

	for coin in coins:
		if (current_change - coin) >= 0:
			coin_number = _least_change(current_change - coin, coins)

			# Find the min of the change below, +1 to include this
			if min > coin_number + 1:
				min = coin_number + 1
				min = coin_number + 1

	return min

def main():
	coins = [25, 10, 5, 1]
	change = 12345
	least = least_change(change, coins, [{}])

	print "Least change for %d is %d" % (change, least)


if __name__ == '__main__':
	main()