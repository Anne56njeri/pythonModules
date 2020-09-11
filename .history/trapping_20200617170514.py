def trap(arr):
    value = max(arr)
    copy = arr
    for i in range(len(arr)):
        del max(arr[i])
    print()    
        
         
trap([3,0,2,0,4])            
