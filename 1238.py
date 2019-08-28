testCases = int(input())
for _ in range(testCases):
	s1,s2 = map(str, input().split())
	if len(s1) > len(s2):
		s5 = s1[len(s2):]
	elif len(s2) > len(s1):
		s5 = s2[len(s1):]
	else:
		s5 = ''
	s3 = list(zip(s1,s2))
	s4 = []
	for i in s3:
		for e in i:
			s4.append(e)
	s4 = ''.join(s4)
	s4 = s4 + s5
	print(s4)

1
aa bb
abab