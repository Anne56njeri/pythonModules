def equi(A):
    # return the number of equal leaders that both occur in the sequences 
    # first find the equileader 
    # then count them in both sequences 
    store = {}
    candidate = -1
    
    for i in A:
        if i in store:
            store[i] +=1 
        else:
            store[i] = 1 
    for i in store:
        if store[i] > (len(A) // 2):
            candidate = i
    countA = 0 
    countB = 0 
    for i in range(len(A)-1):
        countA = A[:i+1].count(candidate)
        countB = A[]
        if candidate in A[:i+1]:
            countA +=1 
        if candidate in A[i+1:]:
            countB +=1 
        if countA == countB:
            return countA        
        
print(equi([4,3,4,4,4,2]))    