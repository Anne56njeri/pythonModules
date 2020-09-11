def oranges(grid):
    if len(grid) == 0:
        return 0 
    rottenQueue = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 2:
                rottenQueue.append([i,j])
            if grid[i][j] == 1:
                        
    

        

oranges( [[2,1,1],[0,1,1],[1,0,1]])            
