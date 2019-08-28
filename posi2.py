a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())

par=0
impar=0
posi=0
nega=0

lista = [a,b,c,d,e]

for _ in lista:
	if _ > 0:
		posi += 1
	if _ < 0:
		nega += 1
	if _ % 2 == 0:
		par += 1
	if _ % 2 != 0:
		impar += 1	


print("%d valor(es) par(es)" % par)
print("%d valor(es) impar(es)" % impar)
print("%d valor(es) positivo(s)" % posi)
print("%d valor(es) negativo(s)" % nega)