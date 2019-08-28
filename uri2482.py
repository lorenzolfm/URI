dictionary = {}
numTranslations = int(input())
for _ in range(numTranslations):
	key = input()
	value = input()
	dictionary.update({key:value})

numCards = int(input())
for _ in range(numCards):
	name = input()
	language = input()
	print(name)
	print(dictionary[language])
	print('')