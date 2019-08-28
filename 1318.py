while True:
	duplicates = []
	ogTics, peopleOnParty = map(int, input().split())
	if ogTics == 0 and peopleOnParty == 0:
		break
	lista = list(map(int, input().split()))
	for i in lista:
		if lista.count(i) > 1 and i not in duplicates:
			duplicates.append(i)
	print(len(duplicates))



