def check(grid,row,column,num):
    # Set grid length to 9
    size = 9

    for i in range(size):
        # Checking if the number is in the same row 9 times
        if grid[row][i] == num: 
          return False
        
    for i in range(size):
        # Checking if the number is in the same column 9 times
       if grid[i][column] == num:
          return False
       # Checking if the same number is in the same square 3 times
       row_0 = (row // 3) * 3
       column_0 = (column // 3) * 3
       for i in range(3):
          for j in range(3):
             if grid[row_0 + i] [column_0 + j] == num:
                return False
             
def solve(grid,row,column,size):
     # 0 is for empty cells
   
    grid = [[4,0,2,5,0,7,6,0,0],
            [5,6,3,0,0,0,0,0,0],
            [0,5,7,0,2,3,0,4,1],
            [0,0,5,0,2,0,8,0,0],
            [7,0,0,6,5,0,0,3,0],
            [0,3,0,2,4,0,0,2,0],
            [2,5,0,0,0,0,0,6,8],
            [0,0,0,0,0,0,0,9,1],
            [0,0,3,4,0,8,4,0,0]]

    # Row and column have to be empty in order to solve the sudoku
    if solve(grid,0,0):
       print(grid)
    else:
      print("error")

     # After reaching the 8th row and 9th column we stop
    if (row == size - 1 and column == size):
       return True
    # If column is 9 then column goes back to 0 and we start going by each row at a time       
    if column == size:
        row += 1
        column = 0
   
    for num in range(1, size + 1, 1):
        # grid has to be greater than 0 to iterate through each cell
       if grid[row][column] > 0:
         return solve(grid,row,column)
        # calling function check and veifying whether this is true
    if check(grid,row,column):
       grid[row][column] == num
    else:
       grid[row][column] == 0
    return False

   
       
   
    
    


    
   

     

   


       

             

             
             
             
       
       
        
        
