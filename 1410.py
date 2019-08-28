while True:
	A,D = map(int, input().split())
	if A == 0 and D == 0:
		break
	dAtacantes = list(map(int, input().split()))
	dDefesa = list(map(int, input().split()))
	dAtacantes.sort()
	dDefesa.sort()
	dDefesa = dDefesa[1::]
	menorDAtacante = min(dAtacantes)
	if menorDAtacante < dDefesa[0]:
		print('Y')
	else:
		print('N')

