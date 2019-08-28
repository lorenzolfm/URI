testCases = int(input())

for _ in range(testCases):
	distances = []
	distance = 0
	numofMembers,selectedNumber = input().split()

	numofMembers = int(numofMembers)
	selectedNumber = int(selectedNumber)

	guesses = list(map(int, input().split()))

	for guess in guesses:
		if guess>= selectedNumber:
			distance = guess - selectedNumber
			distances.append(distance)
		else:
			distance =  selectedNumber - guess
			distances.append(distance)

		print(distances)

