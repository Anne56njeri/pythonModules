def perm(arr):
    # sort the array 
    if len(arr) == 0:
        return 0
    else:

        arr.sort()
        
        perm = set(arr)
        maxValue = max(arr)

        if len(perm) == maxValue:
            return 1
        elif len(perm) == 1 and :
            return 0
               
               
    
print(perm([1,1,1]))