operation = (input())
#Construção da matriz 12x12
matrix = [None] * 12
for line in range(0,12):
	matrix[line] = [None] * 12

#Inserindo os valores
for line in range(0,12):
	for column in range(0,12):
		matrix[line][column] = float(input())

soma = 0
qtde = (144-24)/4

#como o numero de numeros somados cresce e depois desce é mais fácil dividir em dois lacos for
walkerLeft = 1
walkerRight = 11
for line in range(0,5):
	for column in range(walkerLeft,6):
		soma += matrix[line][column]
	walkerLeft +=1
	for column in range(6,walkerRight):
		soma += matrix[line][column]
	walkerRight -= 1


if operation == 'S':
	print('%0.1f' % soma)
else:
	print('%0.1f' % (soma/qtde))