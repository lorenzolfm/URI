notas = []

while len(notas) < 2:
	nota = float(input())
	if nota < 0 or nota > 10 :
		print('nota invalida')
	else:
		notas.append(nota)

media = sum(notas)/len(notas)

print('media = %0.2f' % media)