n = int(input())
quebrados = 0
for i in range(0,n):
	l, c = map(int, input().split())
	if l > c:
		quebrados += c
print(quebrados)