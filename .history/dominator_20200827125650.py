def leader(A):
    # create a dictionary the element that occurs more than n//2 times 
    # once I find it I return the  index 
    store = {}
    candidate = -1
    leader = -1
    for i in A:
        if i in store:
            store[i] +=1 
        else:
            store[i] = 1 
    for i in store:
        if store[i] > (len(A) // 2):
            candidate = i 
            
    for k in range(len(A)):
        if candidate == A[k]:
           
    return leader
              
     
print(leader([3,4,3,2,3,-1,3,3]))              