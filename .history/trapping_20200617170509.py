def trap(arr):
    value = max(arr)
    copy = arr
    for i in range(len(arr)):
        del max(arr[i])
        
        
         
trap([3,0,2,0,4])            
