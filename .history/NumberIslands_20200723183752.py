def mark_current_island()
def Islands(arr):
    # the arr given is a 2 by 2 array 
    if len(arr) == 0:
        return 0

    number_of_islands = 0 
    rows = len(arr)
    cols = 
    for i in range(len(arr)):
        for j in range(arr[i]):
            if arr[i][j] == "1":
                mark_current_island(grid,i,j,rows,cols)
                number_of_islands +=1




Islands([
    ["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]
    ])