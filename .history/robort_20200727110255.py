def uniquePaths(m,n):
    # use dynamic programming and answer is at arr[m][n]
    # let's create and empty grid with 0's 
    grid = [[0 for x in range(m)] for y in range(n)] 
    # print(grid)
    # then using the top down uproach we shall prefill all the 
    # i,j i = 0 and j+1 
    # then i +1 ,j = 0 
    for i in range(len(grid)):
        
        for j in range(len(grid[i])):
           if i == 0 or j == 0:
               
               grid[i][j] = 1 
           else:
               grid[i][j] = grid[i-1][j]    
    print(grid)           
              
                        
uniquePaths(3,2)    