def uniquePath(arr):
    # mark one as None or -1 thatway in the case where 
    # we have to  only calculate the once where there is no none 
    m = len(arr)-1 
    n = len(arr[0])-1
    for i in range(len(arr)):
        for j in  range(len(arr[i])):
            if arr[i][j] == 1:
                arr[i][j] = "None" 
                
            elif i == 0 or j == 0:
                arr[i][j] = 1 
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == "None":
                arr[i][j-1] = 1
                arr[i-1][j] = 1 
                arr[i+1][j] = 1
                arr[i][j+1] = 1 
            else:
                if arr[i-1][j] != "None" and arr[i][j-1] != "None":
                    arr[i][j] = arr[i-1][j] + arr[i][j-1]
          
                    



    
    print(arr[m][n])                         


uniquePath([
  [0,0,0,0],
  [0,1,1,0],
  [0,0,0,0]
])    