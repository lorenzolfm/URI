numeroJogadores = int(input())

totalSaques = 0
totalBloqueios = 0
totalAtaques = 0

totalSaques1 = 0
totalBloqueios1 = 0
totalAtaques1 = 0

estatSaques = 0
estatAtaques = 0
estatBloqueios = 0

for _ in range(0, numeroJogadores):
	nome = str(input())
	s,b,a = input().split()
	s1,b1,a1 = input().split()
	#Formatacao dos inputs
	s = int(s)
	b = int(b)
	a = int(a)
	s1 = int(s1)
	b1 = int(b1)
	a1 = int(a1)
	#Calculo das estatisticas
	totalSaques += s
	totalSaques1 += s1

	totalBloqueios += b
	totalBloqueios1 += b1

	totalAtaques += a
	totalAtaques1 += a1

if totalSaques == 0:
	estatSaques = 0
	estatBloqueios = (totalBloqueios1/totalBloqueios) * 100
	estatAtaques = (totalAtaques1/totalAtaques) * 100

elif totalBloqueios == 0:
	estatSaques = (totalSaques1/totalSaques) * 100
	estatBloqueios = 0
	estatAtaques = (totalAtaques1/totalAtaques) * 100

elif totalAtaques == 0:
	estatSaques = (totalSaques1/totalSaques) * 100
	estatBloqueios = (totalBloqueios1/totalBloqueios) * 100
	estatAtaques = 0

else:
	estatSaques = (totalSaques1/totalSaques) * 100
	estatBloqueios = (totalBloqueios1/totalBloqueios) * 100
	estatAtaques = (totalAtaques1/totalAtaques) * 100

print("Pontos de Saque: %.2f %%." % estatSaques)
print("Pontos de Bloqueio: %.2f %%." % estatBloqueios)
print("Pontos de Ataque: %.2f %%." % estatAtaques)

