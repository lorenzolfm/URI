 #os cidadões são ordenadados de acordo com suas notas (quanto maior, melhor) e recebem descontos no imposto de renda de acordo com sua qualificação.
 #dado o número de habitantes da Nlogônia e todas as notas obtidas, responda as consultas para retornar a nota do cidadão que ficou em determinada posição.
while True:
	try:
		notas = []
		consulta = []
		n,q = input().split()
		n = int(n)
		q = int(q)
		for _ in range(n):
			nota = int(input())
			notas.append(nota)
		notas = sorted(notas,reverse=True)
		for _ in range(q):
			consulta = int(input())
			print(notas[consulta-1])
	except EOFError:
		break