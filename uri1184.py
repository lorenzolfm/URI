operation = input()

#Construindo uma matriz 12x12
matrix = [None] * 12
for line in range(0,12):
	matrix[line] = [None] * 12

#Inserindo data
for line in range(0,12):
	for column in range(0,12):
		matrix[line][column] = float(input())

soma = 0
qtde = (144-12)/2

for line in range(1,12):
	for column in range(0, line):
		soma += matrix[line][column]

#Seleção da operação
if operation == 'S':
	print('%0.1f' % soma)
else:
	print('%0.1f' % (soma/qtde))