numCells = int(input())
cells = []
for _ in range(numCells):
	cell = int(input())
	cells.append(cell)

cells.insert(0, 0)
cells.append(0)
for cell in range(1,numCells+1):
	if cells[cell-1] == 0 and cells[cell] == 0 and cells[cell+1] == 0:
		print(0)
	elif cells[cell-1] == 0 and cells[cell] == 0 and cells[cell+1] == 1:
		print(1)
	elif cells[cell-1] == 0 and cells[cell] == 1 and cells[cell+1] == 0:
		print(1)
	elif cells[cell-1] == 0 and cells[cell] == 1 and cells[cell+1] == 1:
		print(2)
	elif cells[cell-1] == 1 and cells[cell] == 0 and cells[cell+1] == 0:
		print(1)
	elif cells[cell-1] == 1 and cells[cell] == 0 and cells[cell+1] == 1:
		print(2)
	elif cells[cell-1] == 1 and cells[cell] == 1 and cells[cell+1] == 0:
		print(2)
	elif cells[cell-1] == 1 and cells[cell] == 1 and cells[cell+1] == 1:
		print(3)




