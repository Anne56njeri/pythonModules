def discs(A):
    newArr = []
    opendiscks = 0 
    intersections = 0 
    for i in range(len(A)):
        newArr.append((i-A[i]))
    newArr.sort()
    for i in newArr:
        for j in A:
            if i < j:
                opendiscks +=1 
                newArr.remove(i)
            else:
                opendiscks -=1 


discs([1,5,2,1,4,0])        