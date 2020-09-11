def equi(A):
c
    i = 0
    
    while i < len(A)-1:
        array1 = A[i+1:]
        array2 =  A[:i+1]
        if leader(array1) == leader1 and leader(array2) == leader1:
            count +=1
        
        i+=1 
    return count
def leader(A):
    
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
            
    
           
    return candidate
        
           
        
print(equi([1, 2, 3, 4, 5] )) 