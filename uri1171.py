testCases = int(input())
lista = []
for _ in range(testCases):
	n = int(input())
	lista.append(n)

lista = sorted(lista)
dic = {n: lista.count(n) for n in lista}

for key in dic:
	print('%d aparece %d vez(es)' % (key,dic[key]))