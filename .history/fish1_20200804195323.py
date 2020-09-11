def fish(A,B):
    # where A represent the size of fish and B represents the direction of fish 
    
    newFish = {}
    aliveFish = len(A)
    i = 0 
    j = 0 
    while i < len(A) and j < len(B):
        if B[j] == 1 and B[j+1] !=1:
            if A[i] > A[i+1]:
                
            
        
fish([4,3,2,1,5],[0,1,0,0,0])    