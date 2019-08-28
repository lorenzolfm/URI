horas = list(map(int, input().split()))



if horas[0] > horas[1]:
	duracao = 24 - horas[0] + horas[1]
	

if horas[0] == horas[1]:
	duracao = 24

if horas[0] < horas[1]:
	duracao = horas[1] - horas[0]

print('O JOGO DUROU %d HORA(S)'% duracao)