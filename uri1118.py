
notas = []

while True:
	while len(notas) < 2:
		nota = float(input())
		if nota < 0 or nota > 10 :
			print('nota invalida')
		else:
			notas.append(nota)

	media = sum(notas)/len(notas)

	print('media = %0.2f' % media)
	deNovo = int(input('novo calculo (1-sim 2-nao)'))
	if deNovo == 2:
		break
	if deNovo != 1 or deNovo != 2:
		deNovo = int(input('novo calculo (1-sim 2-nao)'))
	notas = []

