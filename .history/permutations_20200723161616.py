def perm(A):
    # sort the array 
    if len(A) == 0:
        return 0  
    else:
        maxValue = max(A)
        perm = set(A)
        if len(perm) = maxValue:
            return 1
        return 0    

               
               
    
print(perm([100,101]))