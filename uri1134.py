lista = []
while True:
	val = int(input())
	if 1<=val<=4:
		if val == 4:
			break
		else:
			lista.append(val)

alcool = lista.count(1)
gasol = lista.count(2)
diesel = lista.count(3)

print("MUITO OBRIGADO")
print("Alcool: %d" % alcool)
print("Gasolina: %d" % gasol)
print("Diesel: %d" % diesel)


