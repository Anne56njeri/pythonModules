def array(n,m):
    # where n is row size  and m is column size 
    array = [[0 for x in range(n)] for x in range(m)]
    print(array) 
    a = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]] 
    # where the first arguement reps the row and second arguement reps the column
    print(a[0][3])

def hourGlass(arr):
    # you have a 2d array 
    # get max hour glass 
    # var maxCount to keep record of the max count 
    # what do you know about an hourglass 
    # the indicies fall in a pattern where 
    # i and i+2 are not equal to 0 and i + 1 is equal to 0 

    maxCount = 1
    if arr !=[]:
        for i in range(arr):
            for j in range(i):
                
    else:
        return 0            
hourGlass([[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,2,4,4],[0,0,0,2,0,0],[0,0]])