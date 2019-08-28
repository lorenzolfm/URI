testCases = int(input())
lista = []
listaUnica = []
for _ in range(testCases):
	num = int(input())
	lista.append(num)
	lista.sort()
for i in lista:
	if i not in listaUnica:
		listaUnica.append(i)
for i in listaUnica:
	ap = lista.count(i)
	print('%d aparece %d vez(es)' % )


