numPeople = int(input())
pool = list(map(int, input().split()))

zeros = pool.count(0)
ones = pool.count(1)

if zeros > ones:
	print('Y')
else:
	print('N')
