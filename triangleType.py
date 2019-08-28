l1, l2, l3 = input().split()
l1 = float(l1)
l2 = float(l2)
l3 = float(l3)
lados = [l1,l2,l3]
lados.sort(reverse = True)
A = lados[0]
B = lados[1]
C = lados[2]
'''
if (A >= B+C):
	print("NAO FORMA TRIANGULO")

elif (A**2) > (B**2 + C**2):
	print("TRIANGULO OBTUSANGULO")
	if A == B and B == C:
		print("TRIANGULO EQUILATERO")
	elif ((A == B) and (B != C)) or ((B == C) and (A != B)):
		print("TRIANGULO ISOCELES")
	elif (A**2) == (B**2 + C**2):
		print("TRIANGULO RETANGULO")
	
elif (A**2) < (B**2 + C**2):
	print("TRIANGULO ACUTANGULO")
	if A == B and B == C:
		print("TRIANGULO EQUILATERO")
	elif ((A == B) and (B != C)) or ((B == C) and (A != B)):
		print("TRIANGULO ISOCELES")
	elif (A**2) == (B**2 + C**2):
		print("TRIANGULO RETANGULO")

else:
	if A == B and B == C:
		print("TRIANGULO EQUILATERO")
	elif ((A == B) and (B != C)) or ((B == C) and (A != B)):
		print("TRIANGULO ISOCELES")
	elif (A**2) == (B**2 + C**2):
		print("TRIANGULO RETANGULO")
'''

if(A>=B+C):
    print("NAO FORMA TRIANGULO")
else:
    if(A**2 == B**2+C**2):
        print("TRIANGULO RETANGULO")
    if(A**2>B**2+C**2):
        print("TRIANGULO OBTUSANGULO")
    if(A**2<B**2+C**2):
        print("TRIANGULO ACUTANGULO")
    if(A==B==C):
        print("TRIANGULO EQUILATERO")
    elif(A==B):
        print("TRIANGULO ISOSCELES")
    elif(A==C):
        print("TRIANGULO ISOSCELES")
    elif(B==C):
        print("TRIANGULO ISOSCELES")
#Tem que botar um if dentro de acutangulo e obtusangulo pra ver se é isoceles ou equilatero

