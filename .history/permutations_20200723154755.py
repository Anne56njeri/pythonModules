def perm(arr):
    # sort the array 
    arr.sort()
    for i in range(len(arr)):
        if arr[i] +1 != arr[i+1]:
            return 1 
            
    
perm([4,1,3,2])