total = 0
c = 0
r = 0
s = 0

entradas = int(input())
for _ in range(entradas):
	quantia,tipo = input().split()
	quantia = int(quantia)
	if tipo == 'C':
		c+=quantia
		total+=quantia
	elif tipo == 'R':
		r+=quantia
		total+=quantia
	else:
		s+=quantia
		total+=quantia

pC = (c/total) * 100
pR = (r/total) * 100
pS = (s/total) * 100

print('Total: %d cobaias' % total)
print('Total de coelhos: %d' % c)
print('Total de ratos: %d' % r)
print('Total de sapos: %d' % s)
print('Percentual de coelhos: %0.2f %%' %pC)
print('Percentual de ratos: %0.2f %%' %pR)
print('Percentual de sapos: %0.2f %%' %pS)