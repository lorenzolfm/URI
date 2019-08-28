n = int(input())
area = 0
for i in range(0,n):
	x, y = input().split()
	x = int(x)
	y = int(y)
	area = (x*y)/2
	print('%d cm2' % area)