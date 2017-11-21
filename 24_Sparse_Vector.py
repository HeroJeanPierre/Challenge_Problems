# Given two dot products compute the dot product

# O(n)
def dot(a, b):
	dot = 0
	ai = 0
	bi = 0

	while ai < len(a) and bi < len(b):
		if a[ai][0] == b[bi][0]:
			dot += a[ai][1]*b[bi][1]

		if a[ai][0] >= b[bi][0]:
			bi += 1
		else:
			ai += 1
	return dot

def genLists():
	from random import randint
	a = []
	b = []

	for i in range(20):
		if randint(1, 3) == 1:
			a.append((i, randint(1, 100)))
		
		if randint(1, 3) == 1:
					b.append((i, randint(1, 100)))

	return a, b

a, b = genLists()

print a
print b

print dot(a, b)