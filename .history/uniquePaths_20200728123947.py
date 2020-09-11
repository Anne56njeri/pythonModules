def uniquePath(obstacleGrid):
    # mark one as None or -1 thatway in the case where 
    # we have to  only calculate the once where there is no none 
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    grid = [[0 for x in range(m)] for y in range(n)] 

    if len(obstacleGrid) == 0 or obstacleGrid[0][0] == 1 or obstacleGrid == None or len(obstacleGrid[0]) == 0:
        return 0
    if obstacleGrid[m-1][n-1] == 1:
        return 0    
    for i in range(m):
        if obstacleGrid[i][0] !=1:
            grid[i][0] = 1
        else:
            # obstacleGrid[i][0] = 0 
            break 

    for j in range(1,n):
        if obstacleGrid[0][j] !=1:
            grid[0][j] = 1
        else:
            # obstacleGrid[0][j] = 0 
            break 
    print(grid) 
    for i in range(1,m):
        for j in range(1,n):
            if obstacleGrid[i][j] != 1:
                grid[i][j] =    
print(uniquePath(
 [[0,0],[1,0]]

  
))   