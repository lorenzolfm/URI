# 0 = norte, 1 = leste, 2 = sul, 3 = oeste
while True:
	position = 90
	numComands = int(input())
	if numComands == 0:
		break
	comands = str(input())
	listofComands = [comand for comand in comands]

	for comand in listofComands:
		if comand.lower() == 'd':
			position -= 90
		elif comand.lower() == 'e':
			position += 90

	#reducao
	position =  position % 360

	if position == 0 or position == 360:
		print('L')
	elif position == 90:
		print('N')
	elif position == 180:
		print('O')
	else:
		print('S')

