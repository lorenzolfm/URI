while True:
	lixo = int(input())
	mary_wins = 0
	john_wins = 0
	if lixo == 0:
		break
	lista = list(map(int, input().split()))
	for i in lista:
		if i == 0:
			mary_wins+=1
		else:
			john_wins += 1
	print('Mary won %d times and John won %d times' % (mary_wins,john_wins))
