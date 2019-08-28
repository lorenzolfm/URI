i = 0
while True:
	r = int(input())
	i += 1
	ganhador = 0
	if r == 0:
		break
	placarA = 0
	placarB = 0
	for x in range(0,r):
		a, b = input().split()
		a = int(a)
		b = int(b)
		placarA += a
		placarB += b
	if placarA > placarB:
		ganhador = 'Aldo'
	if placarB > placarA:
		ganhador = 'Beto'
	print('Teste %d' % i)
	print(ganhador)
	print('')
	


