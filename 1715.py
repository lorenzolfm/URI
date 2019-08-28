numGames, numPlayers = map(int, input().split())
lista = []
marcouEmTodos = 0
for _ in range(numGames):
	scores = list(map(int, input().split()))
	if 0 not in scores:
		marcouEmTodos += 1

print(marcouEmTodos)




