L, A, P, R = input().split()

L = int(L)
A = int(A)
P = int(P)
R = int(R)

d_caixa = [L,A,P]
d_caixa.sort()
menor = d_caixa[0]
meio = d_caixa[1]
maior = d_caixa[2]



raio_real = 0.5*((maior**2 + meio**2 +menor**2)**(1/2))

if raio_real <= R:
	print("S")
else:
	print("N")
'''
raio_real = 0.5*(sqrt(A**2 + (L**2 + P**2)**2)

'''