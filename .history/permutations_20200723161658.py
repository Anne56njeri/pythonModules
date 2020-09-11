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

               
               
    
print(perm([100,101]))