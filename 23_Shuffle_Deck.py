from random import randint

# Pass in 52 card deck, returns shuffled
def shuffle(deck):

	# len(deck) - 1, because the last element doesn't need to be swapped
	for i in range(len(deck) - 1):
		rand_index = randint(i, len(deck) - 1)
		swap(deck, i, rand_index)

def swap(arr, first, second):
	if first == second:
		return

	temp = arr[second]
	del arr[second]
	arr.insert(first, temp)


cards = []

# Create sorted list of cards
for i in range(1, 53):
	cards.append(i)

print cards
shuffle(cards)
print cards
