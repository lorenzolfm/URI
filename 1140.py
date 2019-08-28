while True:
	sentence = list(map(str, input().split()))
	if sentence == ['*']:
		break
	initials = [s[0].lower() for s in sentence]
	if initials.count(initials[0]) == len(initials):
		print('Y')
	else:
		print('N')
