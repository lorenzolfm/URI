# 1 nó  = 1 milha naurtica por hora
TW  = 12
D,VF,VG = input().split()
D = int(D)
VF = int(VF)
VG = int(VG)
X = ((TW*TW)+(D*D))*(1/2)
TF = TW/VF
TG = X/VG

if (TG>TF):
	print('N')
else:
	print('S')