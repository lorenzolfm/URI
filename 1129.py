numofQuestions = 1
while numofQuestions != 0:
	numofQuestions = int(input())
	for _ in range(numofQuestions):
		pxlValues = list(map(int, input().split()))
		if pxlValues[0] <= 127 and pxlValues[1] > 127 and pxlValues[2] > 127 and pxlValues[3] > 127 and pxlValues[4] > 127:
			print('A')
		elif pxlValues[1] <= 127 and pxlValues[0] > 127 and pxlValues[2] > 127 and pxlValues[3] > 127 and pxlValues[4] > 127:
			print('B')
		elif pxlValues[2] <= 127 and pxlValues[1] > 127 and pxlValues[0] > 127 and pxlValues[3] > 127 and pxlValues[4] > 127:
			print('C')
		elif pxlValues[3] <= 127 and pxlValues[1] > 127 and pxlValues[2] > 127 and pxlValues[0] > 127 and pxlValues[4] > 127:
			print('D')
		elif pxlValues[4] <= 127 and pxlValues[1] > 127 and pxlValues[2] > 127 and pxlValues[3] > 127 and pxlValues[0] > 127:
			print('E')
		else:
			print('*')