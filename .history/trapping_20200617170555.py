def trap(arr):
    
    copy = arr
    for i in range(len(arr)):
        value = max(arr[i])
        del value
    print(arr)    
        
         
trap([3,0,2,0,4])            
