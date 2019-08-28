n1,n2,n3,n4 = input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)
avg = (n1*2 + n2*3 + n3*4 + n4)/(2+3+4+1)

print("Media: %.1f" % avg)
if avg >= 7.0:
	print("Aluno aprovado.")
elif avg < 5.0:
	print("Aluno reprovado.")
else:
	print("Aluno em exame.")
	n5 = float(input())
	print("Nota do exame: %.1f" % n5)
	avg = (avg + n5)/2
	if avg >= 5.0:
		print("Aluno aprovado.")
		print("Media final: %.1f" % avg)
	else:
		print("Aluno reprovado.")
		print("Media final: %.1f" % avg)
