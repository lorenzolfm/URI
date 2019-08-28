while True:
	chamada = {}
	diffs = 0
	fakeSignatures = 0
	numStudents = int(input())
	if numStudents == 0:
		break
	for _ in range(numStudents):
		ogStudent, ogSignature = input().split()
		if ogStudent != '':
			chamada.update({ogStudent:ogSignature})
	#print(chamada)

	presentStudents = int(input())
	if presentStudents == 0:
		print(0)
	else:
		for _ in range(presentStudents):
			student, signature = input().split()
			for c in range(len(signature)):
				if signature[c] != chamada[student][c]:
					diffs +=1
			if diffs > 1:
				fakeSignatures += 1
			diffs = 0
		print(fakeSignatures)



	#presentStudents = int(input())
	#if presentStudents == 0:
	#	print(0)
	#else:
	#	for _ in range(presentStudents):
	#		student, signature = input().split()
	#		for c in range(len(signature)):
	#			if signature[c] != chamada[student][c]:
	#				diffs += 1
	#	if diffs > 1:
	#		fakeSignatures += 1
	#	print(fakeSignatures)
