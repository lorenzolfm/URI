vals = list(map(int, input().split()))
a = vals[0]
n = list(filter(lambda x: x > 0, vals[1:]))[0]
soma = 0
for i in range(n):
	soma += a + i
print(soma)