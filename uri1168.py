digits = []
total = 0

testCases = int(input())

for _ in range(testCases):
	number = str(input())
	for digit in number:
		digits.append(digit)
		if digit == '1':
			total += 2
		elif digit == '2':
			total += 5
		elif digit == '3':
			total += 5
		elif digit == '4':
			total += 4
		elif digit == '5':
			total += 5
		elif digit == '6':
			total += 6
		elif digit == '7':
			total += 3
		elif digit == '8':
			total += 7
		elif digit == '9':
			total += 6
		elif digit == '0':
			total += 6
	print('%d leds' % total)	
	digits.clear()
	total = 0

