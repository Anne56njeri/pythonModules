def trap(arr):
    left = max(arr)
    copy = []
    for j in arr:
        copy.append(j)
    
    arr.remove(left)
   
    right = max(arr)
    total = 0
    print(copy)
    for i in range(len(copy)-1):
        total += min(left,right) - copy[i]
        print(min(left,right),"-",copy[i],"==",total)
    print (total)    


          
     

        
         
trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])            
