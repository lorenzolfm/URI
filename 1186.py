operation = input()

array = [None] * 12
for line in range(len(array)):
	array[line] = [None] * 12

for line in range(len(array)):
	for column in range(len(array)):
		array[line][column] = float(input())
sumCells = 0
iterableCells = (144 - 12)/2
step = 11
for line in range(0,12):
	for column in range(11,step,-1):
		# print(line,column)
		sumCells += array[line][column]
	step -= 1

if operation == 'S':
	print('%0.1f' % sumCells)
else:
	print('%0.1f' % (sumCells/iterableCells))