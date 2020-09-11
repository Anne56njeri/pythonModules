def surronded(board):
    # dfs 
    # untouched 
    # in progress 
    # finished 
    rows = len(board)
    if rows == 0:
        return 
    cols = len(board[0])

    if cols == 0:
        return 
    state = [[0]* cols for _ in range(rows)]  
    for x in range(rows):
        for y in range(cols): 
            if [x][y] == '0' and state[x][y] == 0:
                dfs(x,y)
