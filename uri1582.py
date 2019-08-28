import math
def MDC(x,y):
	while y!=0:
		(x,y) = (y,x%y)
	return x

while True:
	try:
		x,y,z = input().split()
		x = int(x)
		y = int(y)
		z = int(z)
		nums = [x,y,z]
		nums = sorted(nums)
		if nums[2] == math.sqrt(nums[0]**2 + nums[1]**2):
			a = MDC(x,y)
			b = MDC(a,z)
			if b == 1:
				print("tripla pitagorica primitiva")
			else:
				print('tripla pitagorica')
		else:
			print('tripla')

	except EOFError:
		break