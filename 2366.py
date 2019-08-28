completed = True
lixo, maxDistanceWithoutWater = map(int, input().split())
waterSpots = list(map(int, input().split()))
waterSpots.append(42195)
intervals = [(waterSpots[i+1] - waterSpots[i]) for i in range(len(waterSpots)-1)]
for interval in intervals:
	if interval > maxDistanceWithoutWater:
		completed = False

if completed:
	print('S')
else:
	print('N')