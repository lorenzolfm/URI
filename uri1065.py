x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())
x5 = int(input())
num = [x1,x2,x3,x4,x5]
pares = 0
for i in num:
	if i % 2 == 0:
		pares+=1
print('%d valores pares' % pares)

