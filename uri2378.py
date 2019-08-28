n,c = input().split()
n = int(n)
c = int(c)
quantosTemDentro = 0
sobrepeso = False
for i in range(0,n):
	s,e= input().split()
	s = int(s)
	e = int(e)
	quantosTemDentro -= s
	quantosTemDentro += e
	if quantosTemDentro > c:
		sobrepeso = True

if sobrepeso == True:
	print('S')
else:
	print('N')
