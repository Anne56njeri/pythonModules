def uniquePath(obstacleGrid):
    # mark one as None or -1 thatway in the case where 
    # we have to  only calculate the once where there is no none 
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    
    if len(obstacleGrid) == 0 or obstacleGrid[0][0] == 1 or obstacleGrid == None or len(obstacleGrid[0]) == 0:
        return 0
        
    for i in range(m):
        if obstacleGrid[i][0] !=1:
            obstacleGrid[i][0] = 1
        else:
            # obstacleGrid[i][0] = 0 
            break 

    for j in range(1,n):
        if obstacleGrid[0][j] !=1:
            obstacleGrid[0][j] = 1
        else:
            # obstacleGrid[0][j] = 0 
            break 
    print(obstacleGrid)
    for i in range(1,len(obstacleGrid)):
        for j in range(1,len(obstacleGrid[0])):
            if  obstacleGrid[i][j] == 0:
                obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]  
            else:
                obstacleGrid[i][j] = 0  
    print(obstacleGrid)                  
    print(obstacleGrid[m-1][n-1]) 
       
uniquePath(
 [[0,0,0],[0,1,0],[0,0,0]]

  
)    