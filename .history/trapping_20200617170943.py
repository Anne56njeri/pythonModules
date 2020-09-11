def trap(arr):
    left = max(arr)
    copy = arr
    arr.remove(left)
    right = max(arr)
    total = 0
    for i in range(len(copy)):
        total = total + min(left,right) - copy[i]
    print(total)    

        
         
trap([0, 1, 0, 2, 1, 0,1, 3, 2, 1, 2, 1])            
