lixo = int(input())
census = list(map(int, input().split()))
favor = census.count(0)
against = census.count(1)
if favor > against:
	print("Y")
else:
	print("N")