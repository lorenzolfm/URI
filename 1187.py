operation = input()

array = [None] * 12
for line in range(len(array)):
	array[line] = [None] * 12

for line in range(len(array)):
	for column in range(len(array)):
		array[line][column] = float(input())

sumCells = 0
iterableCells = (144 - 24)/4
stepFirstHalf = 1
stepSecondHalf = 11

for line in range(0,5):
	for column in range(stepFirstHalf,6):
		# print(line,column)
		sumCells += array[line][column]
	stepFirstHalf += 1

for line in range(0,5):
	for column in range(6,stepSecondHalf):
		# print(line,column)
		sumCells += array[line][column]
	stepSecondHalf -= 1


if operation == 'S':
	print('%0.1f' % sumCells)
else:
	print('%0.1f' % (sumCells/iterableCells))