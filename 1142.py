val = int(input())
odd1 = 1
odd2 = 2
odd3 = 3
for n in range(val):
	print('%d %d %d PUM' % (odd1,odd2,odd3))
	odd1+= 4
	odd2+= 4
	odd3+= 4