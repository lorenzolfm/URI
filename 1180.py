lixo = input()

lista = list(map(int, input().split()))
a = min(lista)
pos = lista.index(a)
print('Menor valor: %d' % a)
print('Posicao: %d' % pos)