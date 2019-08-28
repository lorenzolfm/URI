jumpHeight, numofPipes = input().split()
jumpHeight = int(jumpHeight)
numofPipes = int(numofPipes)
pipeHeights = list(map(int, input().split()))
defeat = False

heightDifference = [abs(j-i) for i,j in zip(pipeHeights[:-1], pipeHeights[1:])]

for height in heightDifference:
	if height > jumpHeight:
		print('GAME OVER')
		defeat = True
		break
if defeat == False:
	print('YOU WIN')

	#calcular |h(n) - h(n+1)|
	#se a diferenca > salto -> game over


