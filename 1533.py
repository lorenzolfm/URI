while True:
	lixo = int(input())
	if lixo == 0:
		break
	suspectLevel = list(map(int, input().split()))
	sorted_suspectLevel = sorted(suspectLevel, reverse = True)
	secondMostSuspect = sorted_suspectLevel[1]
	print(suspectLevel.index(secondMostSuspect) + 1)