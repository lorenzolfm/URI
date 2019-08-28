operation = str(input())

matrix = [None] * 12
for line in range(len(matrix)):
	matrix[line] = [None]*12

#input
for line in range(0,12):
	for column in range(0,12):
		matrix[line][column] = float(input())

soma = 0
quantity = (144-24)/4
stepDecrease = 10
stepIncrease = 7
for line in range(1,6):
	for column in range(11,stepDecrease,-1):
		soma += matrix[line][column]
	stepDecrease -= 1
for line in range(6,11):
	for column in range(stepIncrease,12):
		soma+= matrix[line][column]
	stepIncrease += 1

if operation == 'S':
	print('%0.1f' % soma)
else:
	print('%0.1f' % (soma/quantity))
