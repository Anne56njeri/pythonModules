def oranges(grid):
    if len(grid) == 0:
        return 0 

    rottenQueue = []
    row = len(grid)
    col = len(grid[i])
    fresh = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 2:
                rottenQueue.append([i,j])
            elif grid[i][j] ==1:
                fresh +=1 
    while len(rottenQueue) > 0:
        num = len(rottenQueue)
        for i in range(num):
            x,y = rottenQueue[0]
            rottenQueue.pop(0)
            if x > 0 and grid[x-1][y] == 1:
                grid[x-1][y] = 2
                rottenQueue.append(grid[x-1,y])   
                fresh -=1 
            if y > 0 and grid[]                 
           
                        
    

        

oranges( [[2,1,1],[0,1,1],[1,0,1]])            
