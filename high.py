l=[]
for item in range(0, 5):
	a = int(input())
	l.append(a)
	b = max(l)
	c = l.index(b) + 1
print(b)
print(c)