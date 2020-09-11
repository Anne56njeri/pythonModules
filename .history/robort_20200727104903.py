def uniquePaths(m,n):
    # use dynamic programming and answer is at arr[m][n]
    # let's create and empty grid with 0's 
    grid = [[0] * m] * n
    # then using the top down uproach we shall prefill all the 
    # i,j i = 0 and j+1 
    # then i +1 ,j = 0 
uniquePaths(3,2)    