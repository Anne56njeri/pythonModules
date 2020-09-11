def discs(A):
    newArr = []
    opendiscks = 0 
    intersections = 0 
    for i in range(len(A)):
        newArr.append((i-A[i]))
    newArr.sort()
    
    i = 0 
    j = 0 
    while i < len(newArr) and j < len(A):
        if newArr[i]< A[j]:
            opendiscks
            i+=1 




discs([1,5,2,1,4,0])        