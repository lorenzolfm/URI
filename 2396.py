totalTimes = {}
runners, laps = map(int, input().split())
for runner in range(runners):
	lapTimes = list(map(int, input().split()))
	totalTimes[runner+1] = sum(lapTimes)
for _ in range(3):
	winner = min(totalTimes, key=totalTimes.get) 
	print(winner)
	
	
