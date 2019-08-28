n = int(input())

vetor = list(map(int, input().split()[:n]))
minimo = min(vetor)
indice = vetor.index(minimo)
print('Menor valor: %d' % minimo)
print('Posicao: %d'% indice)

