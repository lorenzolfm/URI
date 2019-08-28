while True:
	n = int(input())
	if n == 0:
		break
	jogo = list(map(int, input().split()))
	marryGanhou = jogo.count(0)
	johnGanhou = jogo.count(1)
	print("Mary won %d times and John won %d times" %(marryGanhou,johnGanhou))