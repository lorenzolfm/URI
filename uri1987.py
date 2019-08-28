while True:
	try:		
		numAlgs, number = input().split()
		numAlgs = int(numAlgs)
		number = str(number)
		Algs = []
		for i in number:
			Algs.append(int(i))
		soma = sum(Algs)
		if soma % 3 == 0:
			print('%d sim' % soma)
		else:s
			print('%d nao' % soma)
	except EOFError:
		break


while True:
    try:
        n, m = input().split()
        r = 0
        for i in range(len(m)):
            r += int(m[i])
        m = str(r)
        print(m, end=' ')
        if int(m) % 3 == 0:
            print('sim')
        else:
            print('nao')
        
    except EOFError:
        break




