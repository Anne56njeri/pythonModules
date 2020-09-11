def perm(arr):
    # sort the array 
    if len(arr) == 0:
        return 0
    else:

        arr.sort()
        for i in range(len(arr)-1):
            if arr[i] +1 != arr[i+1]:
                return 
        return 0        
    
print(perm([4,1,3,2]))