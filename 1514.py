while True:
	arrayPlayers = []
	obtainedConditions = 0
	numPlayers, numProblems = map(int, input().split())
	if numPlayers == 0 and numProblems == 0:
		break
	for player in range(numPlayers):
		answers = list(map(int, input().split()))
		arrayPlayers.append(answers)

	#Condicao 1
	condition1 = 0
	for answers in arrayPlayers:
		if 0 in answers:
			condition1+=1
	if condition1 == numProblems:
		obtainedConditions += 1

	#Condition 4
	condition3 = 0
	for answers in arrayPlayers:
		if sum(answers) == 0:
			condition3 += 1
	if condition3 == 0:
		obtainedConditions += 1

	#Condicao 2 e 3 tem que fazer a lista de cada problema
	arrayProblems = [[arrayPlayers[j][i] for j in range(len(arrayPlayers))] for i in range(len(arrayPlayers[0]))]
	#Condicao 2
	condition2 = 0
	for problem in arrayProblems:
		if 1 in problem:
			condition2 += 1
	if condition2 != 0:
		obtainedConditions += 1

	#Condicao 3 Nao ha nenhum problema resolvido por todos
	condition3 = 0
	for problem in arrayProblems:
		if sum(problem) == numProblems:
			condition3 += 1
	if condition3 == 0:
		obtainedConditions += 1
	

	





			

	print(obtainedConditions)
