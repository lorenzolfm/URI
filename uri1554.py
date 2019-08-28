
import math

casos = int(input())
bolaMaisProx = 9999999999

while casos:
	numeroBolas = int(input())
	x, y = list(map(int, input().split()))
	casos -= 1

for bolas in range(0,numeroBolas):
	xn, yn = list(map(int, input().split()))
	distancia = math.sqrt(abs(x - xn)**2 + abs(y - yn)**2)
	numeroBolas -= 1
	if distancia<bolaMaisProx:
		bolaMaisProx = distancia
		nBola = bolas + 1

print(nBola)
