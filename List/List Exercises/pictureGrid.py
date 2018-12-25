grid = [['.', '.', '.', '.', '.', '.'],
	['.', 'O', 'O', '.', '.', '.'],
	['O', 'O', 'O', 'O', '.', '.'],
	['O', 'O', 'O', 'O', 'O', '.'],
	['.', 'O', 'O', 'O', 'O', 'O'],
	['O', 'O', 'O', 'O', 'O', '.'],
	['O', 'O', 'O', 'O', '.', '.'],
	['.', 'O', 'O', '.', '.', '.'],
	['.', '.', '.', '.', '.', '.']]
def pictureGrid(list):
	for i in range(len(list )-3):
		print()
		for j in range(len(list)):
			print(list[j][i], end='')
		
	print()
pictureGrid(grid)
