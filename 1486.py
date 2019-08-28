while True:
	somaMaior = 0
	p,n,c = map(int, input().split())
	if p == 0 and n == 0 and c == 0:
		break
	for i in range(n):
		lista = list(map(int, input().split()))
		if sum(lista) >= c:
			somaMaior+=1
	print(somaMaior)


