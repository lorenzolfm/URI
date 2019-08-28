def func(sm,nH,H):
	for i in range(nH):
		for j in range(numHouses):
			s = houses[i]+houses[j]
			if s == sm:
				val1 = houses[i]
				val2 = houses[j]	
				return val1,val2


numHouses = int(input())
houses = []
for _ in range(numHouses):
	house = int(input())
	houses.append(house)
soma = int(input())

r = func(soma,numHouses,houses)

print('%d %d' % (r[0],r[1]))


