a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

i=0

lista = [a,b,c,d,e,f]

for _ in lista:
	if _ > 0:
		i += 1

print("%d valores positivos" % i)
