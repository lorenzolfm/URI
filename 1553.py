while True:
	addedQuestions = 0
	lixo, k = map(int, input().split())
	if lixo == 0 and k == 0:
		break
	timesQuestionWasAsked = list(map(int, input().split()))
	