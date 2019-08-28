n = int(input())
for _ in range(n):
	divs = []
	test = int(input())
	for i in range(1,test+1):
		if test % i == 0:
			divs.append(i)
	if len(divs)>2:
		print('%d nao eh primo' % test)
	else:
		print('%d eh primo' % test)
