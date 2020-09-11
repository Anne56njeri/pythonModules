def perm(arr):
    # sort the array 
    if len(arr) == 0:
        return 0
    else:

        arr.sort()
        perm = set(arr)
        maxValue = max()
        if len(perm) == maxValue
        for i in range(len(arr)-1):
            if arr[i] +1 != arr[i+1]:
                return 0
        return 1       
    
print(perm([1,1,1]))