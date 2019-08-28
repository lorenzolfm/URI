valores = list(map(int, input().split()))
naoOrdenado = [valores[0],valores[1],valores[2]]

valores.sort()
for i in valores:
	print(i)
print('')
for n in naoOrdenado:
	print(n)