totalTimes = {}
runners, laps = map(int, input().split())
for runner in range(runners):
	lapTimes = list(map(int, input().split()))
	totalTimes[runner+1] = sum(lapTimes)
print(min(totalTimes, key=totalTimes.get))