def surronded():
    # dfs 
    # untouched 
    # in progress 
    # finished 
    rows = len(board)
    if rows == 0:
        return
    cols = len(board[0])