count = 0
while True:
	winner = None
	count += 1
	lixo = int(input())
	if lixo == 0:
		break
	tickNumber = list(map(int, input().split()))
	for ticket in tickNumber:
		if ticket == (tickNumber.index(ticket) + 1):
			winner = ticket
	print('Teste %d' % count)
	print(winner)
	print('')