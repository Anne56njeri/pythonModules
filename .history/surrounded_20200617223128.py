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
        canReach = False
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for dx,dy in directions:
            nextX,nextY = dx+x,dy+y
        if nextX < 0 or nextX >= rows or nextY < 0 or nextY >= cols:
            canReach = True
            continue 
        


    for x in range(rows):
        for y in range(cols): 
            if [x][y] == '0' and state[x][y] == 0:
                if canReachOutside(x,y,pending):
                    # process states to change from o  to x
                    pass
                else:
                    # regulary process states 
                    pass
