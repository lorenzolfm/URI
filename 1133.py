x = int(input())
y = int(input())
vals = []
if x < y:
	for n in range(x+1,y):
		if n%5 == 2 or n%5 == 3:
			vals.append(n)
else:
	for n in range(y+1,x):
		if n%5 == 2 or n%5 == 3:
			vals.append(n)
vals.sort()
for val in vals:
	print(val)