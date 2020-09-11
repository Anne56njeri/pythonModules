def perm(arr):
    # sort the array 
    if len(arr) == 0:
        return 0
    else:

        arr.sort()
        for i in range(len(arr)):
            if arr[i] +1 != arr[i+1]:
                return 1 
        return 0        
    
perm([4,1,3,2])