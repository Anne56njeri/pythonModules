def trap(arr):
    for i in range(len(arr)-1):
        # find the maximum on its left 
        left = arr[i] 
        print
        for j in range(i):
            left = max(left,arr[j])
            print(left) 
trap([3,0,2,0,4])            
