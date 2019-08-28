#Função a ser usada para dividir matrix por colunas
def chunks(l, n):
	for i in range(0, len(l), n):
		yield l[i:i+n]

#Algoritmo
while True:
	#Declaracao de variavel saida e dos inputs de dimensao da matriz
	char = 0
	numPeople, numProblems = input().split()
	numPeople = int(numPeople)
	numProblems = int(numProblems)
	#Condição de quebra do loop
	if numPeople == 0 and numProblems == 0:
		break 

	#Construção da matriz de dimensões numPeople x numQuestions
	solutions = [None] * numPeople
	for line in range(0,numPeople):
		solutions[line] = [None] * numProblems
	#inserção dos dados na matriz
	for i in range(numPeople):
		answers = list(map(int, input().split()))
		solutions[i] = answers

	#Verificação das condições

	#Condição 1: Ninguém resolveu todos os problemas.
	isAllProblemsSolved = True
	for person in range(len(solutions)):
		listOfProblemsPerPerson = solutions[person]
		if sum(listOfProblemsPerPerson) == numProblems:
			isAllProblemsSolved = False
		if isAllProblemsSolved == True:
			char += 1

	#Condição 4: Todos resolveram ao menos um problema (não necessariamente o mesmo).
	isAtLeastOneProblemSolvedPerPerson = True
	for person in range(len(solutions)):
		sumOfProblemsPerPerson = sum(solutions[person])
		if sumOfProblemsPerPerson == 0:
			isAtLeastOneProblemSolvedPerPerson = False
	if isAtLeastOneProblemSolvedPerPerson == True:
		char += 1

	#As condições 2 e 3 necessitam analisar o grupo das mesmas questões
	#Desse modo, vamos organizar uma lista que contem listas dos acertos/erros da mesma questão
	i = 0
	questionsArray = []
	while i < numProblems:
		for person in range(len(solutions)):
			questionsArray.append(solutions[person][i])
		i+=1
	chunk = list(chunks(questionsArray, numProblems))

	#Condição 2: Todo problema foi resolvido por pelo menos uma pessoa (não necessariamente a mesma).
	isAllProblemSolvedAtLeastOne = True
	for answers in range(len(chunk)):
		sumOfSolved = sum(chunk[answers])
		if sumOfSolved == 0:
			isAllProblemSolvedAtLeastOne = False
		if isAllProblemSolvedAtLeastOne == True:
			char +=1
	#Condição 3: Nao há nenhum problema resolvido por todos
	allPeopleSolved = True
	for answers in range(len(chunk)):
		sumOfSolved1 = sum(chunk[answers])
		if sumOfSolved1 == numProblems:
			allPeopleSolved = False
		if allPeopleSolved == True:
			char += 1

	print(char)