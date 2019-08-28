C, P, F  =  map(int, input().split())

folhas_por_pessoa_exato = (P/F)


if folhas_por_pessoa_exato >= C:
	print("S")
else:
	print("N")