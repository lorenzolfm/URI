testCases = int(input())
totalPrice = 0
totalKg = 0
for i in range(testCases):
	spent = float(input())
	fruits = list(map(str, input().split()))
	kg = float(spent/2)
	totalPrice += spent
	totalKg += kg
	print('day %d: %0.0f kg' % ((i+1),kg))

avgPriceDay = totalPrice/testCases
avgKgDay = totalKg/testCases

print('%0.2f kg by day' % avgKgDay)
print('R$ %0.2f by day' % avgPriceDay)
