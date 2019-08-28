testCases = int(input())
for _ in range(testCases):
	num = int(input())
	divs = [i for i in range(1,num+1) if num % i == 0 and i != num]
	soma = sum(divs)
	if soma == num:
		print('%d eh perfeito' % num)
	else:
		print('%d nao eh perfeito' % num)
