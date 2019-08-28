# tickets = []
# fakeTickets = 0
# while True:
# 	n,m = input().split()
# 	n = int(n)
# 	m = int(m)
# 	if n == 0 and m == 0:
# 		break
# 	tickets = list(map(int, input().split()))
# 	for ticket in tickets:
# 		moreThenOne = tickets.count(ticket)
# 		tickets = list(filter(lambda a: a != ticket, tickets))
# 		print(tickets)
# 		if moreThenOne > 1:
# 			fakeTickets += moreThenOne
# 	print(fakeTickets)
# 	tickets = []

tickets = []
originalTickets = 0
fakeTickets = 0
while True:
	n,m = input().split()
	n = int(n)
	m = int(m)
	if n == 0 and m == 0:
		break
	tickets = list(map(int, input().split()))
	for ticket in tickets:
		numAppearences = tickets.count(ticket)
		tickets.remove(ticket)
		if numAppearences > 1:
			fakeTickets += numAppearences - 1
	print(fakeTickets)
	tickets = []
