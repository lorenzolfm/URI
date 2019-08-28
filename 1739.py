fib_cache={}
def fib(x):
	if x in fib_cache:
		return fib_cache[x]
	if x <= 2:
		return 1
	val = fib(x-1)+fib(x-2)
	fib_cache[x] = val
	return val

for i in range(100):
	fib(i)


fib3 = []
for i in fib_cache:
	if '3' in str(fib_cache[i]) or fib_cache[i] % 3 == 0:
		fib3.append(fib_cache[i])


while True:
	try:
		n = int(input())
		print(fib3[n-1])
	except EOFError:
		break
