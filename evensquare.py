n = int(input())

lista = [x for x in range(1,n+1) if x % 2 == 0]

for item in lista:
	square = item**2
	print("%d^2 = %d" % (item, square))