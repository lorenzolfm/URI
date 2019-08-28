lados = list(map(int, input().split()))
lados.sort()

a = lados[2]
b = lados[1]
c = lados[0]

if (a >= (b+c)) or (b >= (a+c)) or (c >= (a+b)):
	print('Invalido')

else:
	
	if a != b != c:
		print('Valido-Escaleno')
		if a**2 == b**2 + c**2:
			print('Retangulo: S')
		else:
			print('Retangulo: N')
	
	elif a == b == c:
		print('Valido-Equilatero')
		if a**2 == b**2 + c**2:
			print('Retangulo: S')
		else:
			print('Retangulo: N')
	
	else:
		print('Valido-Isoceles') 
		if a**2 == b**2 + c**2:
			print('Retangulo: S')
		else:
			print('Retangulo: N')