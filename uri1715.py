numPlayers, numGames = input().split()
numPlayers = int(numPlayers)
numGames = int(numGames)
counter = 0
matrix = []

for player in range(numPlayers):
	gameScores = list(map(int, input().split()))
	matrix.append(gameScores)

for player in range(len(matrix)):
	if 0 not in matrix[player]:
		counter += 1

print(counter)

# matrix = [None] * numPlayers
# for player in range(len(matrix)):
# 	matrix[player] = [None] * numGames

# for player in range(len(matrix)):
# 	for game in range(len(matrix[player])):
# 		matrix[player][game] = int(input())

# for player in range(len(matrix)):
# 	print(matrix[player])
