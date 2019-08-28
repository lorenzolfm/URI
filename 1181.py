operationLine = int(input())
operation = input()

array = [None] * 12
for line in range(len(array)):
	array[line] = [None] * 12

for line in range(len(array)):
	for column in range(len(array)):
		array[line][column] = float(input())

sumCells = 0
iterableCells = 12

for column in range(0,12):
	sumCells += array[operationLine][column]



if operation == 'S':
	print('%0.1f' % sumCells)
else:
	print('%0.1f' % (sumCells/iterableCells))