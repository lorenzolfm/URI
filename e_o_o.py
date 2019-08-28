'''
n = int(input())

for i in range(1,n+1):
	a = int(input())
	if (a % 2 == 0) and (a > 0):
		print("EVEN POSITIVE")
	if (a % 2 == 0) and (a < 0):
		print("EVEN NEGATIVE")
	if (a % 2 != 0 ) and (a > 0):
		print("ODD POSITIVE")
	if (a % 2 == 0) and (a < 0):
		print("ODD NEGATIVE")
	if (a == 0):
		print("NULL")

l=[]
a=int(input())
for n in range(1,(a+1)):
    l.append(int(input()))
for n in l:
    if (n%2!=0) and (n<0):
        print("ODD NEGATIVE")
    if(n==0):
        print("NULL")
    if(n%2!=0) and (n>0):
        print("ODD POSITIVE")
    if(n%2==0) and (n<0):
        print("EVEN NEGATIVE")
    if(n%2==0) and (n>0):
        print("EVEN POSITIVE")
'''
N = int(input())
for c in range(0, N):
  num = int(input())
  if num % 2 == 0 and num > 0:
    print('EVEN POSITIVE')
  elif num % 2 == 0 and num < 0:
    print('EVEN NEGATIVE')
  elif num % 2 == 1 and num > 0:
    print('ODD POSITIVE')
  elif num % 2 == 1 and num < 0:
    print('ODD NEGATIVE')
  else:
    print('NULL')