def fish(A,B):
    # where A represent the size of fish and B represents the direction of fish 
    
    newFish = {}
    totalFish = len(A)
    for i,j in zip(A,B):
        newFish[i] = j 
        
    