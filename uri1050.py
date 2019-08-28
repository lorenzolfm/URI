ddd = int(input())
dictDDD = {'Brasilia': 61, 'Salvador': 71, 'Sao Paulo': 11, 'Rio de Janeiro': 21, 'Juiz de Fora': 32, 'Campinas': 19, 'Vitoria': 27, 'Belo Horizonte': 31}
if ddd not in dictDDD.values():
	print('DDD nao cadastrado')
else:
	key_list = list(dictDDD.keys())
	val_list = list(dictDDD.values())
	print(key_list[val_list.index(ddd)])
