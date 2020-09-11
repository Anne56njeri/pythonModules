def Islands(arr):
    # the arr given is a 2 by 2 array 
    if len(arr) == 0:
        return 0

    number_of_islands = 0 
    for i in range(len(arr)):
        for j in range(arr[i]):
            if arr[i][j] == ""



Islands([
    ["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]
    ])