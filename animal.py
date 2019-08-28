ossos = str(input())
classe = str(input())
hab_alimentar = str(input())

if ossos == "vertebrado":

	if classe == "ave":
		if hab_alimentar == "carnivoro":
			print("aguia")
		if hab_alimentar == "onivoro":
			print("pomba")

	if classe == "mamifero":
		if hab_alimentar == "onivoro":
			print("homem")
		if hab_alimentar == "herbivoro":
			print("vaca")

if ossos == "invertebrado":

	if classe == "inseto":
		if hab_alimentar == "hematofago":
			print("pulga")
		if hab_alimentar == "herbivoro":
			print("lagarta")

	if classe == "anelideo":
		if hab_alimentar == "hematofago":
			print("sanguessuga")
		if hab_alimentar == "onivoro":
			print("minhoca")
