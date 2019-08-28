testCases = int(input())
lista = {}
for _ in range(testCases):
	dispProducts = int(input())
	for _ in range(dispProducts):
		fruit, price = input().split()
		price = float(price)
		lista[fruit] = price
	total = 0
	wannaBuy = int(input())
	for _ in range(wannaBuy):
		key,qnt = input().split()
		qnt = int(qnt)
		price = lista[key]*qnt
		total += price
	print('R$ %0.2f' % total)




