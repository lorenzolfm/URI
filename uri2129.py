import math
i = 0
while True:
	try:
 		i += 1
		n = int(input())
		fact = math.factorial(n)
		digits = [i for i in str(fact)]
		digits = [int(i) for i in digits]
		digits.reverse()
		digits = [ i for i in digits if i != 0]
		print('Instancia %d' % digits)
		print(digits[0])
 	except EOFError:
 		break
