column = int(input())
operation = input()

matrix = [None] * 12
for linha in range(0,12):
	matrix[linha] = [None] * 12 #Cria matriz 12x12

for linha in range(0,12):
	for coluna in range(0,12):
		matrix[linha][coluna] = float(input()) #Le os 144 valores da matriz

soma = 0

for linha in range(0,12):
	soma += matrix[linha][column]

if operation =='S':
	print('%0.1f' % soma)
else:
	print('%0.1f' % (soma/12))


