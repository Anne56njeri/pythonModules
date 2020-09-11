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
        pending.append(x,y)
        canReach = False
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for dx,dy in directions:
            nextX,nextY = dx+x,dy+y
        if nextX < 0 or nextX >= rows or nextY < 0 or nextY >= cols:
            canReach = True
            continue 
        
        if board[nextX][nextY] == 'O' and state[nextX][nextY] == 0:
            state[nextX][nextY] = 1
            canReach != canReachOutside(nextX,nextY,pending)
        return canReach    


    for x in range(rows):
        for y in range(cols): 
            if [x][y] == '0' and state[x][y] == 0:
                pending = []
                if not canReachOutside(x,y,pending):
                    for pendx,pendy in pending:
                        board[pendx][pendy] = 'X'
                for pendx,pendy in pending:
                        board[pendx][pendy] = 2    
                else:
                    # regulary process states 
                    pass
