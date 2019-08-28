while True:
	lista = []
	x = int(input())
	if x == 0:
		break
	for n in range(1,x+1):
		lista.append(n)
	print(*lista)
