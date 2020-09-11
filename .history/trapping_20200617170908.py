def trap(arr):
    left = max(arr)
    copy = arr
    arr.remove(left)
    right = max(arr)
    total = 0
    for i in range(len(copy)):
        total = total + min(left,right) - copy[i]

        
         
trap([3,0,2,0,4])            
