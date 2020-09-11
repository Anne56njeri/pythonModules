def discs(A):
    newArr = []
    opendiscks = 0 
    intersections = 0 
    for i in range(len(A)):
        newArr.append((i-A[i]))
    newArr.sort()
    
    print(newArr)            


discs([1,5,2,1,4,0])        