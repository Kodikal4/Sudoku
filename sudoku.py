size = 9
def puzzle(array):
    for i in range(size):
        for j in range(size):
            print(array[i][j],end = " ")
        print()
def check(grid, row, col, num):
    for i in range(size):
        if grid[row][i] == num:
            return False
             
    for i in range(size):
        if grid[i][col] == num:
            return False
 
 
    initialRow = row - row % 3
    initialCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + initialRow][j + initialCol] == num:
                return False
    return True
 
def Solve(grid, row, col):
 
    if (row == size - 1 and col == size):
        return True
    if col == size:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return Solve(grid, row, col + 1)
    for num in range(1, size + 1, 1): 
     
        if Solve(grid, row, col, num):
         
            grid[row][col] = num
            if Solve(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False
 
'''0 means the cells where no value is assigned'''
grid = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
        [0, 1, 0, 0, 0, 4, 0, 0, 0],
    [4, 0, 7, 0, 0, 0, 2, 0, 8],
    [0, 0, 5, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 9, 8, 1, 0, 0],
    [0, 4, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 3, 6, 0, 0, 7, 2],
    [0, 7, 0, 0, 0, 0, 0, 0, 3],
    [9, 0, 3, 0, 0, 0, 6, 0, 4]]
 
if (Solve(grid, 0, 0)):
    puzzle(grid)
else:
    print("No solution")
