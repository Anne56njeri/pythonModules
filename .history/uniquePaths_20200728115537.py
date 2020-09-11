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
            obstacleGrid[i][0] = 0 
            break 

    for j in range(1,n):
        if obstacleGrid[0][j] !=1:
            obstacleGrid[0][j] = 1
        else:
            obstacleGrid[0][j] = 0 
            break 
    for i in range(len(obstacleGrid)):
        for j in range(len(ob))    
    print(obstacleGrid) 
       
uniquePath([
  [0,0],
  [1,0],
  
])    