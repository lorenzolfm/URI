testCases = int(input())

for _ in range(testCases):
	M = []
	k = 0

	while k < 5:
		temp = input().split()

		if temp:
			M.append(list(map(int, temp)))
			k += 1
	print(M)		
#logica pra ver se existe um caminho
