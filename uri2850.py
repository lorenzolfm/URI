dicionario ={"esquerda":"ingles",
			"direita":"frances",
			"nenhum":"portugues",
			"as duas":"caiu"}
while True:
	try:
		ent = input()
		print(dicionario[ent])
	except EOFError:
		break
