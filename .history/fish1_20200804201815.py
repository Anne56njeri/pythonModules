def fish(A,B):
    # where A represent the size of fish and B represents the direction of fish 
    
    aliveFish = len(A)
    bigFish = 0
    indexFish = None
    
    j = 0 
    while j < len(B)-1:
        if B[j] == 1 and B[j+1] !=1:
            if A[j] >A[j+1]:
                

        j +=1
         
    print(aliveFish)   
            
        
fish([4,3,2,1,5],[0,1,0,0,0])    