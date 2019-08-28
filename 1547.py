testCases = int(input())
for _ in range(testCases):
	correctAnswer = False
	lixo, correctNumber = map(int, input().split())
	guesses = list(map(int, input().split()))
	distancesGuessCorretNumber = [abs(correctNumber - guess) for guess in guesses]
	indexOfclosestAnswer =  distancesGuessCorretNumber.index(min(distancesGuessCorretNumber)) + 1
	
	for guess in guesses:
		if guess == correctNumber:
			indexOfRightAnswer = guesses.index(guess) + 1
			correctAnswer = True
	if correctAnswer:
		print(indexOfRightAnswer)
	else:
		print(indexOfclosestAnswer)

