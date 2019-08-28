x = int(input())
y = int(input())
impares = [0]
if x < y:
	num = list(range(x+1,y))
elif x > y:
	num = list(range(y+1,x))
else:
	num = [0]

for i in num:
	if i % 2 != 0:
		impares.append(i)

print(sum(impares))

