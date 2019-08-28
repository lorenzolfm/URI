grenais = 0
vitoriasGremio = vitoriasInter = empates = 0
while True:
	grenais += 1
	golsInter, golsGremio = map(int, input().split())
	if golsGremio > golsInter:
		vitoriasGremio += 1
	elif golsInter > golsGremio:
		vitoriasInter += 1
	else:
		empates += 1
	jogar_novamente = int(input('Novo grenal (1-sim 2-nao)\n'))
	if jogar_novamente == 2:
		break


print('%d grenais' % grenais)
print('Inter:%d' % vitoriasInter)
print('Gremio:%d' % vitoriasGremio)
print('Empates:%d' % empates)
if vitoriasInter > vitoriasGremio:
	print('Inter venceu mais')
elif vitoriasGremio > vitoriasInter:
	print('Gremio venceu mais')
else: print('Nao houve vencedor')