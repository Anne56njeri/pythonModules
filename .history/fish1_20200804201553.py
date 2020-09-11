def fish(A,B):
    # where A represent the size of fish and B represents the direction of fish 
    
    aliveFish = len(A)
   
    indexFish = None
    
    newFish = []
    for i,j in zip(A,B):
        newArr = []
        newArr.append(i)
        newArr.append(j)
        newFish.append(newArr)
    i = 0 
    bigFish = [0,0]
    while i < len(newFish):
        if newFish[i][1] == 1 and newFish[i+1][1] !=1:
            if newFish[i][0] >
            
            
        
fish([4,3,2,1,5],[0,1,0,0,0])    