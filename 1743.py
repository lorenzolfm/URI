x = list(map(int, input().split()))
y = list(map(int, input().split()))
z = [0 if i == 1 else 1 for i in y]
if z == x:
	print('Y')
else:
	print('N')