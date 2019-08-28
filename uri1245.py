while True:
	try:
		numBoots = int(input())
		arrayRight = []
		arrayLeft = []
		pairs = 0
		for i in range(numBoots):
			size, side = input().split()
			if side == 'D':
				arrayRight.append(size)
			else:
				arrayLeft.append(size)
		for item in arrayRight:
			if item in arrayLeft:
				pairs += 1
				arrayLeft.remove(item)
		print(pairs)
	except EOFError:
		break