while True:
	try:
		n,m = map(int, input().split())
		matrix = []
		for i in range(n):
			linha = list(map(int,input().split()))
			matrix.append(linha)
		#Deve retornar uma matriz 9 se existe um pao de queijo na posicao i j, se não houver, deve contar o numero de pdq adjacentes
		
	except EOFError:
		break