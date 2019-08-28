while True:

	n = int(input())
	if n == 0:
		break
	for i in range(n):
		alternativas = list(map(int, input().split()))
		for x in range(alternativas):
			if alternativas[x] <= 127:
				
