def MDC(x,y):
	while y!=0:
		(x,y) = (y,x%y)
	return x


testCases = int(input())

for i in range(testCases):
	a,b = input().split()
	a = int(a)
	b = int(b)
	print(MDC(a,b))