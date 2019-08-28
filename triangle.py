a,b,c = input().split()
a = float(a)
b = float(b)
c = float(c)

if (a < b+c) and (b < a+c) and (c < a+b):
	#calcula o perimetro
	p = a+b+c
	print("Perimetro = %.1f" % p)
else:
	#calcula area do trapezio de bases a e b e altura c
	ar = ((a+b)*c)/2
	print("Area = %.1f" % ar)