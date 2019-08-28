n = int(input())
dentro = 0
fora = 0
lista = []
intervalo = [10,11,12,13,14,15,16,17,18,19,20]

for i in range(0,n):
	x = int(input())
	lista.append(x)

for i in lista:
	if i in intervalo:
		dentro += 1
	elif i not in intervalo:
		fora += 1

print('%d in' % dentro)
print('%d out' % fora)