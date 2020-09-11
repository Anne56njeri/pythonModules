def equi(A):
     # return the number of equal leaders that both occur in the sequences 
    # first find the equileader 
    # an equileader is an index such that when two sequences are formed 
    # the two sequences have the same  leader 
    # 0,1,2,3,4,5
    store = {}
    leader1 = 0
    count = 0
    for i in A:
        if i in store:
            store[i] +=1 
        else:
            store[i] = 1 
    for i in store:
        if store[i] > (len(A) // 2):
            leader1 = i 
    count = 0 
    last_idx = 0        
    for i in range(len(A)):
        if A[i] == leader1:
            count +=1 
            last_idx = i 
    if count < len(A) // 2:
        return 0 
    equi_count = 0 
    count_left = 0 
    for i in range(len(A)):
        if A[i] == leader1:
            count_left +=1 
        if count_left > (i+1) // 2 and  count - count_left > (len(A)-i-1) //2:
            equ              


        
           
equi([4,3,4,4,4,2])            