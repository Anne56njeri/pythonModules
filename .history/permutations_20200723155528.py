def perm(arr):
    # sort the array 
    if len(arr) == 0:
        return 0
    else:

        arr.sort()
        for i in range(len(arr)):
            
        perm = set(arr)
        maxValue = max(arr)

        if len(perm) == maxValue:
            return 1
        else:
            return 0    
               
    
print(perm([1,1,1]))