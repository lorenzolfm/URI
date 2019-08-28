

while True:
	try:
		numAtt = int(input())
		nM,nL = map(int, input().split())
		bM = []
		bL = []
		for i in range(nM):
			cM = list(map(int, input().split()))
			bM.append(cM)
		for i in range(nL):
			cL = list(map(int, input().split()))
			bL.append(cL)

		pM,pL = map(int, input().split())

		att = int(input())

		ceM = bM[pM-1]
		ceL = bL[pL-1]

		attM = ceM[att-1]
		attL = ceL[att-1]
		if attM > attL:
			print('Marcos')
		elif attL > attM:
			print('Leonardo')
		else:
			print('Empate')
	except EOFError:
		break

