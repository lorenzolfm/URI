casos  = int(input())

for i in range(casos):
	x = int(input())
	lista = [num for num in range(1,x+1)]
	div = []
	for n in lista:
		if x % n == 0:
			div.append(n)
	if len(div) == 2:
		print('%d eh primo' % x)
	else:
		print('%d nao eh primo' % x)
