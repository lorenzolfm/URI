while True:
	d,n = map(str, input().split())
	lista = []
	if d == '0' and n == '0':
		break
	for c in n:
		if c != d:
			lista.append(c)
	if len(lista) == 0:
		print(0)
	else:
		a = ''.join(str(x) for x in lista)
		print(int(a))

