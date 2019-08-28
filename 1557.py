while True:
	ordem = int(input())
	if ordem == 0:
		break
	#criação da matrix vazia
	else:
		if ordem == 1:
			print(1)
			#print('')
		else:
			matrix = [None] * ordem
			for line in range(ordem):
				matrix[line] = [None] * ordem
			#Mudando os valores
			for line in range(ordem):
				val = 2
				val = val ** line
				for column in range(ordem):
					matrix[line][column] = val
					val += val
			#Impressao da matrix
			for line in range(len(matrix)):
				espaco = ' '*ordem
				print(espaco)
				for column in range(len(matrix)):
					print(str(matrix[line][column]).rjust(ordem), end=" ")
			print('')

				

