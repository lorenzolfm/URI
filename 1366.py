while True:
	ladosIguais = 0
	diffLenghts = int(input())
	if diffLenghts == 0:
		break
	for _ in range(diffLenghts):
		lenght, qnt = map(int, input().split())
		if qnt > 1:
			if qnt % 2 != 0:
				qnt -= 1
			ladosIguais += qnt
	rect = ladosIguais//4
	print(rect)
