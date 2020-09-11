def fish(A,B):
    # where A represent the size of fish and B represents the direction of fish 
    i = 0 
    j = 0 
    newFish = {}
    for i,j in zip(A,B):
        newFish[i] = j 
        
    