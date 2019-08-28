testCases = int(input())
lista = []

for n in range(testCases):
	result = 0
	lista.clear()
	game = str(input())

	for char in game:
		lista.append(char)

	num1 = int(lista[0])
	gameMode = lista[1]
	num2 = int(lista[2])
	isAllUppercase = gameMode.isupper() and gameMode.isalpha()
	if  isAllUppercase ==  True:
		if lista[0] != lista[2]:
			result = num2 - num1
		elif lista[0] == lista[2]:
			result = num1 * num2
	elif isAllUppercase == False:
		if lista[0] != lista[2]:
			result = num1 + num2
		elif lista[0] == lista[2]:
			result = num1 * num2
	print(result)

