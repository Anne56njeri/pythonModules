def trap(arr):
    left = max(arr)
    copy = arr
    arr.remove(left)
    right = max(arr)
    total = 0
    print(left,right)
    for i in range(len(copy)):
        total += (min(left,right) - copy[i])
        

          
     

        
         
trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])            
