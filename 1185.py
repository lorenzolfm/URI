op = input()

matrix = [None] * 12
for line in range(0,12):
	matrix[line] = [None] * 12

#Inserindo os valores
for line in range(12):
	for column in range(12):
		matrix[line][column] = float(input())

qtde = (144-12)/2
soma = 0

for line in range(12):
	for column in range(12 - line - 1):
		soma += matrix[line][column]

if op == 'S':
	print('%0.1f' % soma)
else:
	print('%0.1f' % (soma/qtde))
