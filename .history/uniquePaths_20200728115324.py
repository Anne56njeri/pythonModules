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
                

uniquePath([
  [0,0],
  [1,0],
  
])    