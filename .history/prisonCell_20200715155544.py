def cell (cells,N):
    i = 1 
    while i < len(cells)-1:
        print('i',i-1,'i+1',i+1)
        if (cells[i+1] == cells[i-1]) :
            cells[i] = 1
        else:
        cells[i] = 0    
        i +=1    
    print(cells)    
cell([0,1,0,1,1,0,0,1],7)    