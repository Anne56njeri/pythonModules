def cell (cells,N):
    i = 1 
    while i < len(cells)-1:
        if (cells[i] != cells[i-1]) or cells[i] != cells[i+1]:
            cells[i] = 1
        i +=1    
        
cell([0,1,0,1,1,0,0,1],7)    