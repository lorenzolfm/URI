n = int(input())
#A saída deve conter apenas uma linha contendo a área da região do 
#mar realmente aproveitada pelos pescadores, ou seja,
# a área total da região do mar coberta por pelo menos uma rede
for i in range(0,n):
	xi, xf, yi, yf = input().split()
	xi = int(xi)
	xf = int(xf)
	yi = int(yi)
	yf = int(yf)


# area de uma rede, menos a outra menos a interseccao entre as redes