f_cache = {}
def f(n):
	if n in f_cache:
		return f_cache[n]
	counter = 0
	if n < 2:
		counter = 1
		return counter
	counter = 1+f(n-1)+f(n-2)
	#Retornar ultimo digito na base binaria
	f_cache[n] = counter
	return counter

n = int(input())

print(f(n))