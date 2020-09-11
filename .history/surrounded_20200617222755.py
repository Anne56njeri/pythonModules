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
    def canReachOutside(x,y,pending):
         directions = [(1,0),(-1,0),(0,1),]

    for x in range(rows):
        for y in range(cols): 
            if [x][y] == '0' and state[x][y] == 0:
                if canReachOutside(x,y,pending):
                    # process states to change from o  to x
                    pass
                else:
                    # regulary process states 
                    pass
