jump, n = map(int, input().split())
pipes = list(map(int, input().split()))
diffs = [abs(pipes[i]-pipes[i+1]) for i in range(len(pipes)-1)]
win = True
for i in diffs:
	if i > jump:
		win = False
if win:
	print('YOU WIN')
else:
	print('GAME OVER')