def trap(arr):
    left = max(arr)
    copy = arr
    arr.remove(left)
    right = max(arr)
    print(left,right)
        
         
trap([3,0,2,0,4])            
