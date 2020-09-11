def equi(A):
    # return the number of equal leaders that both occur in the sequences 
    # first find the equileader 
    # then count them in both sequences 
    store = {}
    # candidate = -1
    count = 0
    for i in A:
        if i in store:
            store[i] +=1 
        else:
            store[i] = 1 
    for i in store:
        if store[i] > (len(A) // 2):
            # candidate = i
            count = store[i]
    return count // 2      
     
           
        
print(equi([4, 4, 2, 5, 3, 4, 4, 4] ))    