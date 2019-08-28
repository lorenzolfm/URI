
quadrado = []
somaMagica = 0
zeros = 0

for _ in range(3):
	inputt = list(map(int, input().split()))
	quadrado.append(inputt)


for linha in quadrado:
	if 0 not in linha:
		somaMagica = sum(linha)

if somaMagica == 0:
	quadradoT = list(zip(*quadrado)) 
	for linha in quadrado:
		if 0 not in linha:
			somaMagica = sum(linha)

if somaMagica == 0:
	i = 0
	for linha in quadrado:
		if 0 not in linha:
			somaMagica += linha[i] 
			i += 1

if somaMagica == 0:
	quadradoT = list(zip(*quadrado))
	i = 0
	for linha in quadrado:
		if 0 not in linha:
			somaMagica += linha[i] 
			i += 1

	
for linha in quadrado:
	if 0 in linha:
		soma = sum(linha)
	for i in range(len(linha)):
		if linha[i] == 0:
			linha[i] = somaMagica-soma


for linha in quadrado:
	print('%d %d %d' % (linha[0],linha[1],linha[2]))

