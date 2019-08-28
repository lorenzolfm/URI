c,q = input().split()
c = int(c)
q = int(q)

if c == 1:
	p = q*4.00
	print("Total: R$ %.2f" % (p))


if c == 2:
	p = q*4.50
	print("Total: R$ %.2f" % (p))


if c == 3:
	p = q*5.00
	print("Total: R$ %.2f" % (p))


if c == 4:
	p = q*2.00
	print("Total: R$ %.2f" % (p))


if c == 5:
	p = q*1.50
	print("Total: R$ %.2f" % (p))

