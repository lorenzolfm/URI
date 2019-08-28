casos = int(input())
divisores = []
for i in range(casos):
	x = int(input())
	divisores = [ a for a in range(1,x) if x % a == 0]
	if sum(divisores) == x:
		print('%d eh perfeito' % x)
	else:
		print('%d nao eh perfeito' % x)
