n = int(input())

gods = []
names = []
powers = []
kills = []
deaths = []
for i in range(n):
	name, power, kill, death = input().split()
	power = int(power)
	kill = int(kill)
	death = int(death)
	gods.append([name,power,kill,death])
for i in range(len(gods)):
	names.append(gods[i][0])
	powers.append(gods[i][1])
	kills.append(gods[i][2])
	deaths.append(gods[i][3])
print(names,powers,kills,deaths)


print(gods)