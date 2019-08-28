testCases = int(input())
gbeh = 0
bbeh = 0
childs = []
for _ in range(testCases):
	behv,child = input().split()
	childs.append(child)
	if behv == '+':
		gbeh += 1
	else:
		bbeh += 1
childs = sorted(childs)

for child in childs:
	print(child)
print('Se comportaram: %d | Nao se comportaram: %d' % (gbeh,bbeh))
