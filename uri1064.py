lista = []
for i in range(0,6):
	val = float(input())
	lista.append(val)
listaPosi = [x for x in lista if x >= 0]
media = sum(listaPosi)/len(listaPosi)
print('%d valores positivos' % len(listaPosi))
print('%0.1f' % media)