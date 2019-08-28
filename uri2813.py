testCases = int(input())
homeUmbrellas = 0
officeUmbrellas = 0

for i in range(testCases):
	going, coming = input().split()
	
	if going == 'chuva' and coming == 'sol':
		homeUmbrellas += 1
	elif going == 'sol' and coming == 'chuva':
		officeUmbrellas += 1
	