n = int(input())
totalCobaias = 0
totalCoelhos = 0
totalRatos = 0
totalSapos = 0
percentualCoelhos = 0
percentualRatos = 0
percentualSapos = 0

for i in range(0,n):
	quantia,tipo = input().split()
	quantia = int(quantia)
	tipo = str(tipo)
	totalCobaias += quantia
	if tipo == 'C':
		totalCoelhos += quantia
	elif tipo == 'R':
		totalRatos += quantia
	elif tipo == 'S':
		totalSapos += quantia

percentualCoelhos = (totalCoelhos/totalCobaias)*100
percentualRatos = (totalRatos/totalCobaias)*100
percentualSapos = (totalSapos/totalCobaias)*100

print('Total: %d cobaias' % totalCobaias)
print('Total de coelhos: %d' % totalCoelhos)
print('Total de ratos: %d' % totalRatos)
print('Total de sapos: %d' % totalSapos)
print('Percentual de coelhos: %0.2f %%' % percentualCoelhos)
print('Percentual de ratos: %0.2f %%' % percentualRatos)
print('Percentual de sapos: %0.2f %%' % percentualSapos)