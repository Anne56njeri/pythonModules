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
        if candidate in 
        print('A',A[:i+1])
        print('B',A[i+1:])
equi([4,3,4,4,4,2])    