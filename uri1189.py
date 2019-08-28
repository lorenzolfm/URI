operation = input()
#criacao da matriz
matrix = [None] * 12
for line in range(0,12):
	matrix[line] = [None] * 12
#leitura dos elementos
for line in range(0,12):
	for column in range(0,12):
		matrix[line][column] = float(input())

soma = 0
# quantidade em um triangulo é total - 2*diagonais / 4

qtde = (144-24)/4

#duas laços para somar
#um pra parte superior da matriz
#outra pra parte inferior da matriz
for line in range(0,6):
	for column in range(0,line):
		soma += matrix[line][column]
		print(line, column)
		print('')
for line in range(6,12):
	for column in range(0, 12-line-1):
		soma += matrix[line][column]
		print(line, column)
		print('')


if operation == 'S':
	print('%0.1f' % soma)
else:
	print('%0.1f' % (soma/qtde))