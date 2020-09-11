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
    maxCount = 1
    for i in range(arr):
        for j in range()  