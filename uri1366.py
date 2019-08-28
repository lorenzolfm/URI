while True:
	counter = 0
	numDiffLenghts= int(input())
	listOfQuantity = []
	if numDiffLenghts != 0:
		for _ in range(numDiffLenghts):
			lenght, numSticks = input().split()
			lenght = int(lenght)
			numSticks = int(numSticks)
			listOfQuantity.append(numSticks)
		while sum(listOfQuantity) >= 2:
			for item in range(len(listOfQuantity)):
				if listOfQuantity[item] > 1:
					listOfQuantity[item] -= 2
					counter += 0.5
				else:
					listOfQuantity[item] = 0
	else:
		break
	print(int(counter))
