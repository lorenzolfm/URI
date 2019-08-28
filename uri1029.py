#memoizacao
f_cache = {}
fib_cache = {}
def f(n):
	if n in f_cache:
		return f_cache[n]
	counter = 0
	if n < 2:
		counter = 1
		return counter
	counter = 1+f(n-1)+f(n-2)
	f_cache[n] = counter
	return counter


def fib(x):
	if x in fib_cache:
		return fib_cache[x]
	if x <= 2:
		return 1
	val = fib(x-1)+fib(x-2)
	fib_cache[x] = val
	return val

testCases = int(input())

for i in range(testCases):
	num = int(input())
	a = f(num)
	b = fib(num)
	print('fib(%d) = %d calls = %d' % (num,a-1,b))