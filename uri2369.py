n = int(input())
conta = 0

if n <= 10:
	conta = 7
elif(10<n<=30):
	c0 = n - 10
	conta = 7 + 1*c0
elif(30<n<=100):
	c1 = n - 30
	n = n - c1
	c0 = n - 10
	conta = 7 + 1*c0 + 2*c1 
else:
	c2 = n - 100
	n = n - c2
	c1 = n - 30
	n = n - c1
	c0 = n - 10	
	conta =  7 + 1*c0 + 2*c1 + 5*c2

print(conta)
