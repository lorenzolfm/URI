testCases = int(input())
for _ in range(testCases):
	palavras = list(map(str, input().split()))
	palavras = sorted(palavras,key = len, reverse = True)
	a = ' '.join((str(x) for x in palavras))
	print(a)
