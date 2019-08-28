while True:
	try:
		epr = 0
		ehd = 0
		intrusos = 0
		nAlunos = int(input())
		for n in range(nAlunos):
			lixo,sigla = map(str, input().split())
			if sigla.lower() == 'epr':
				epr += 1
			elif sigla.lower() == 'ehd':
				ehd += 1
			else:
				intrusos += 1
		print('EPR: %d' % epr)
		print('EHD: %d' % ehd)
		print('INTRUSOS: %d' % intrusos)

	except EOFError:
		break