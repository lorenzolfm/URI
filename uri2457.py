letter = str(input())
numOfAppearences = 0
words = list(map(str, input().split()))

for word in words:
	if letter in word:
		numOfAppearences += 1
		

numWords = len(words)
percent = numOfAppearences/numWords * 100
print('%0.1f' % percent)