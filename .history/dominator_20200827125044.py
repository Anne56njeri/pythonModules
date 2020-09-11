def leader(A):
    # create a dictionary the element that occurs more than n//2 times 
    # once I find it I return the  index 
    store = {}
    for i in A:
        if i in store:
            store[i] +=1 
        else:
            store[i] = 1 
    print(store)  
leader([3])              