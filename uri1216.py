avg = 0
distances = []

while True:
	try:
		name = str(input())
		distance = int(input())
		distances.append(distance)
	except EOFError:
		avg = sum(distances)/len(distances)
		print('%0.1f' %avg)	
		break



