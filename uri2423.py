a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
numeroBolos=0


propXicaras = int(a/2)
propOvos = int(b/3)
propLeite = int(c/5)

if propLeite == propOvos == propXicaras:
	numeroBolos = propXicaras
	print('%d' % numeroBolos)
else:
	lista = [propXicaras, propOvos, propLeite]
	lista.sort()
	numeroBolos = lista[0]
	print('%d' % numeroBolos)
