val = int(input())
for n in range(1,val+1):
	a = n*n
	b = (a*n)
	print('%d %d %d' % (n,a,b))
	a = (n*n) + 1
	b = b + 1
	print('%d %d %d' % (n,a,b))