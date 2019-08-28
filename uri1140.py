while True:
	phrase = list(map(str, input().split()))
	equal = True
	if phrase == ['*']:
		break
	firstLetters = [word[0].lower() for word in phrase]
	nTemp = firstLetters[0]
	for item in firstLetters:
		if nTemp != item:
			equal = False
			break
	if equal == True:
		print("Y")
	else:
		print("N")


