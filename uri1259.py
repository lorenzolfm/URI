testCases = int(input())
par = []
impar = []
for _ in range(testCases):
	n = int(input())
	if n % 2 == 0:
		par.append(n)
	else:
		impar.append(n)

par = sorted(par)
impar = sorted(impar, reverse = True)


for i in par:
	print(i)
for j in impar:
	print(j)