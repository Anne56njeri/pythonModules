def markrotten(i,j,row,column,grid):
    # taking care of boundary cases
    if (i < 0 or i >= row  or j < 0 or j >= column) or grid[i][j] !=1:
        
        return 
   

        grid[i][j] == 2
        print('grid',grid)   
        # checking its neighbours
        markrotten(i+1,j,row,column,grid)  
        markrotten(i,j+1,row,column,grid) 
        markrotten(i,j-1,row,column,grid) 
        markrotten(i-1,j,row,column,grid)  
        
        
    


    

def oranges(grid):
    if len(grid) == 0:
        return 0
    # loop through the grid 
    # if there is no fresh orange just return 0 
    # if there is a two check all its four neighbours 
    # recursive call 
    # count when a one becomes a two 
    row = len(grid)
    column = len(grid[0])
    minutes = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 2:
                markrotten(i,j,row,column,grid)
                minutes +=1
            
    print(minutes)  
    print(grid)          

        

oranges( [[2,1,1],[0,1,1],[1,0,1]])            
