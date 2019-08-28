from math import factorial
c = 1
while True:
	try:
		f = 1
		n = int(input())
		f = factorial(n)
		f = str(f)
		r = [i for i in f if i != '0']
		print('Instancia %d' % c)
		print(int(r[-1]))
		c += 1
	except EOFError:
		break