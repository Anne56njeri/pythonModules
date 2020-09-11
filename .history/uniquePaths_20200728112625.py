def uniquePath(arr):
    # mark one as None or -1 thatway in the case where 
    # we have to  only calculate the once where there is no none 
    m = len(arr)-1 
    n = len(arr[0])-1
    
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i == 0 or j == 0:
                if arr[i][j] == 0 
                arr[i][j] =1 
            else:
                arr[i][j] = 0 
                break 
            elif arr[i][j] == 1:
                arr[i][j] = 0    

                                



               
          
                    



    
    print(arr)                         


uniquePath([
  [0,0,0,0],
  [0,1,1,0],
  [0,0,0,0]
])    