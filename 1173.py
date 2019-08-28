vetor = []
n  = int(input())
vetor.append(n)
print('N[0] = %d' % n)
for i in range(9):
	n *= 2
	vetor.append(n)
	indice = i+1
	print('N[%d] = %d' % (indice,n))