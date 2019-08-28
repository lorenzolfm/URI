while True:
	try:
		codes = []
		testCases = int(input())
		for _ in range(testCases):
			code = str(input())
			codes.append(code)
			codes = sorted(codes, reverse = True)
		for code in codes[::-1]:
			print(code)
	except EOFError:
		break