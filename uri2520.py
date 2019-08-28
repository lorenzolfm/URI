while True:
	try:
		pokemonI = playerI = pokemonJ = playerJ = 0
		time = 0
		lines,columns = input().split()
		lines = int(lines)
		columns = int(columns)
		maping = []
		for lines in range(lines):
			mapLayout = list(map(int, input().split()))
			maping.append(mapLayout)
		#Achar posicao coluna do pokemon e players
		for line in range(len(maping)):
			if sum(maping[line]) == 2 or sum(maping[line]) == 3:
				pokemonI = line + 1
				pokemonJ = maping[line].index(2) + 1
			if sum(maping[line]) == 1 or sum(maping[line]) == 3:
				playerI = line + 1
				playerJ = maping[line].index(1) + 1
			
			# else:
			# 	# print(maping[line].index(2),maping[line].index(1))
			# 	time = abs(maping[line].index(2) - maping[line].index(1))
			# 	print(time)
			
		time = abs(pokemonI-playerI) + abs(pokemonJ-playerJ)
		print(time)	

		# print(pokemonI,playerI)	
		# print(pokemonJ,playerJ)

		#Logica do menor caminho
		
		


	except EOFError:
		break