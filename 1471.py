while True:
	try:
		foram, voltaram = map(int, input().split())
		lVoltaram = list(map(int, input().split()))
		if foram == voltaram:
			print('*')
		elif foram != voltaram:
			lForam = list(range(1,foram))
			nao_voltaram = [i for i in lForam if i not in lVoltaram]
			for i in nao_voltaram:
				print(i, sep=' ', end=' ', flush=False)
			print('')
	except EOFError:
		break