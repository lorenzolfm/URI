op = input()

matrix = [None] * 12
for line in range(12):
	matrix[line] = [None] * 12

#Input
for line in range(12):
	for column in range(12):
		matrix[line][column] = float(input())

qtde = (144 - 24)/4
soma = 0
#dividir trabalho por dois
#primeira metade
c = 5
for line in range(6,12):
	for column in range(5,c,-1):
		soma+=matrix[line][column]
	c -= 1
#segunda
d = 6
for line in range(6,12):
	for column in range(6,d):
		soma += matrix[line][column]
	d+=1

if op == 'S':
	print('%0.1f' % soma)
else:
	print('%0.1f' % (soma/qtde))

