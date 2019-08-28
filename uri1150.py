x = int(input())
i = 1
soma = x
while True:
	z = int(input())
	if z>x:
		break


while soma < z:
	i += 1
	x += 1
	soma += x

print(soma)
print(i)