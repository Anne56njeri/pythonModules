def perm(A):
    # sort the array 
    if len(A) == 0:
        return 0  
    else:
        maxValue = max(A)
        perm = set(A)
        if len(perm) != maxValue:
            return 0
        else:
            newPerm = list(perm)
            if len(newPerm) == 1 and newPerm[0] == 1:
                return 0
        return 1           

def permu(A):
    maxValue = max(A)
    newArr = range(1,maxValue)
    perm = {}
    check = set(A)
    if len(A) == 0:
        return 0
    if len(A) == 1 and A[0]!=1:
        return 0 
    for
    for i in newArr:
        if  i in check:
            perm[i] = 1 
        else:
            perm[i] = 0
                
    for x in perm:
        
        if perm[x] == 0:
            return 0
    return 1                 
           
print(permu([1,1]))

               
    