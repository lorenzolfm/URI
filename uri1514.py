def chunks(l, n):
    for i in range(0, len(l), n):
    	yield l[i:i+n]

while True:
	char = 0
	numPeople, numProblems = input().split()
	numPeople = int(numPeople)
	numProblems = int(numProblems)

	if numPeople == 0 and numProblems == 0:
		break 
	#construção da matriz com resultados das questoes
	solutions = [None] * numPeople
	for line in range(0,numPeople):
		solutions[line] = [None] * numProblems
	#inserção dos dados na matriz
	for i in range(numPeople):
		answers = list(map(int, input().split()))
		solutions[i] = answers

	#verificação das condições
	#Condição 1
	conditionOne = True
	for line in range(len(solutions)):
		soma = solutions[line]
		if sum(soma) == numProblems:
			conditionOne = False
	if conditionOne == True:
		char += 1
	#Condição 4
	conditionFour = True
	for solution in range(len(solutions)):
		somaConditioinFour = sum(solutions[solution])
		if somaConditioinFour == 0:
			conditionFour = False
	if conditionFour == True:
		char += 1
	# As condições 2 e 3 necessitam analisar as colunas da matriz
	i = 0
	arrayQuestoes = []
	while i < numProblems:
		for line in range(len(solutions)):
			arrayQuestoes.append(solutions[line][i])
		
		i += 1

	chunk = list(chunks(arrayQuestoes, numPeople))
	#Condição 2
	conditionTwo = True
	for answers in range(len(chunk)):
		somaConditionTwo = sum(chunk[answers])
		if somaConditionTwo == 0:
			conditionTwo = False
	if conditionTwo == True:
		char += 1
	#Condiçao 3 nao ha nenhum problema resolvido por todos
	conditionThree = True
	for answers in range(len(chunk)):
		somaConditionThree = sum(chunk[answers])
		if somaConditionThree == numPeople:
			conditionThree = False
	if conditionThree == True:
		char += 1


	
	

	print(char)