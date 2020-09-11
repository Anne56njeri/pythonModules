def equi(A):
    # return the number of equal leaders that both occur in the sequences 
    # first find the equileader 
    # an equileader is an index such that when two sequences are formed 
    # the two sequences have the same  leader 
    # 0,1,2,3,4,5
    store = {}
    leader = -1
    count = 0
    for i in A:
        if i in store:
            store[i] +=1 
        else:
            store[i] = 1 
    for i in store:
        if store[i] > (len(A) // 2):
            leader = i
    i = 0 
    while i < len(A)-1:
        array1 = A[i+1:]
        array2 =  A[:i+1]
        print(leader(array2))
        # if leader(array1) == leader and leader(array2) == leader:
        #     count +=1
        i+=1
    
def leader(A):
    print('a',A)
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
            return k
           
    return leader
        
           
        
equi([4, 4, 2, 5, 3, 4, 4, 4] )  