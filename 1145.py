fibonacci = [0,1]
b = int(input())
for n in range(46):
	a = fibonacci[-2] + fibonacci[-1]
	fibonacci.append(a)

printedFib = fibonacci[:b]
print(*printedFib)
