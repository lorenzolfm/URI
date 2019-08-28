n1 = 0
n2 = 1

while n1 != n2:
	n1, n2 = input().split()
	n1 = int(n1)
	n2 = int(n2)
	if n1 < n2:
		print('Crescente')
	elif n1 > n2:
		print('Decrescente')
