numRocks, numFrogs = input().split()
numFrogs = int(numFrogs)
numRocks = int(numRocks)
tracker = [0 for num in range(numRocks)]

for frog in range(numFrogs):
	position, jumpDistance = input().split()
	position = int(position)
	jumpDistance = int(jumpDistance)
	#ajustar para comecar a contar do zero
	position -= 1
	#mudar a posicao atual dele na lista pra 1
	tracker[position] = 1
	#calcular para quais posições ele pode pular e mudar essas posições
	willLandRight = position + jumpDistance
	willLandLeft = position - jumpDistance
	#tem que fazer uma logica pra ele saber se existem pedras que ele consegue pular
	if willLandLeft >= 0 and willLandRight <= len(tracker):
		tracker[willLandRight] = 1
		tracker[willLandLeft] = 1

for val in tracker:
	print(val)





