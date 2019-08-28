comprimento,nGotas = map(int, input().split())
posi = list(map(int, input().split()))

posicaoMaisEsquerda = posi[0]
d = posicaoMaisEsquerda-1

posi = posi[1::]

for i in posi:
	diferenca = int((i - posicaoMaisEsquerda)/2)
	if diferenca > d:
		d = diferenca
	posicaoMaisEsquerda = i

if (comprimento - posicaoMaisEsquerda > d):
	d = comprimento - posicaoMaisEsquerda

print(d)