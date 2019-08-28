rocks, frogs = map(int, input().split())
rep = [0] * rocks
for _ in range(frogs):
	initialPos, jump = map(int, input().split())
	initialPos -= 1
	salva_init = initialPos
	rep[initialPos] = 1
	for i in range(rocks):
		if initialPos - jump >= 0:
			landedback = initialPos - jump
			initialPos = landedback
			rep[landedback] =  1
	initialPos = salva_init
	for i in range(rocks):
		if initialPos + jump < len(rep):
			landedfoward = initialPos + jump
			initialPos = landedfoward
			print(landedfoward)
			if landedfoward >= len(rep) + 1:
				rep[landedfoward - 1] = 1
			else:
				rep[landedfoward] = 1
for i in rep:
	print(i)
