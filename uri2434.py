n, saldo = input().split()
n = int(n)
saldo = int(saldo)
historico = []
for i in range(0,n):
	movimentacao = int(input())
	saldo += movimentacao
	historico.append(saldo)
historico.sort()
menorSaldo = historico[0]
print(menorSaldo)

