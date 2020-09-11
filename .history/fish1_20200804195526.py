def fish(A,B):
    # where A represent the size of fish and B represents the direction of fish 
    
    aliveFish = len(A)
    bigFish = 0
    i = 0 
    j = 0 
    while i < len(A) and j < len(B):
        if B[j] == 1 and B[j+1] !=1:
            if A[j] > A[j+1]:
                aliveFish -=1
                if A[j] > bigFish:
                    bigFish = A 
            elif A[j+ 1] > A[j]:
                aliveFish -=1   
            
        
fish([4,3,2,1,5],[0,1,0,0,0])    