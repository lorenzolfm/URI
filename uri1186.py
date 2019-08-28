#inputs
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
qtde = (144 - 12)/2
context = 0
for line in range(11,0, -1):
	for column in range(11, 0 + context, -1):
		soma += matrix[line][column]
	context += 1

if operation == 'S':
	print('%0.1f' % soma)
else:
	print('%0.1f' % (soma/qtde))

