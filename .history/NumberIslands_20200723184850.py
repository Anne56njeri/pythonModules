def mark_current_island(arr,i,j,row,col):
    # take care of the boundary cases 
    if(i < 0 or i >=row  or j < 0 or j >= col) or arr[i][j] !="1":
        # means just exit the function
        return
    arr[i][j] = ""    



def Islands(arr):
    # the arr given is a 2 by 2 array 
    if len(arr) == 0:
        return 0

    number_of_islands = 0 
    # row size
    rows = len(arr)
    # column size 
    cols = len(arr[0])
    for i in range(len(arr)):
        for j in range(arr[i]):
            if arr[i][j] == "1":
                mark_current_island(arr,i,j,rows,cols)
                number_of_islands +=1

    return number_of_islands


Islands([
    ["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]
    ])