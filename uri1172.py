vetor = []
for i in range(10):
	n = int(input())
	vetor.append(n)

for n, i in enumerate(vetor):
	if i == 0 or i < 0:
		vetor[n] = 1

for n, i in enumerate(vetor):
	valor = vetor[n]
	print('X[%d] = %d' % (n,valor))