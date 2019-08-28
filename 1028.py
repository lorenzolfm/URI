def MDC(a,b):
	if b == 0:
		return a
	return MDC(b,a%b)

testCases = int(input())
for _ in range(testCases):
	a,b = map(int, input().split())
	print(MDC(a,b))
