def surronded():
    # dfs 
    # untouched 
    # in progress 
    # finished 
    rows = len(board)
    if rows == 0:
        return 
    if cols == 0:
        return 
    state = [[0]* cols]        
    cols = len(board[0])