def discs(A):
    newArr = []
    opendiscs = 0 
    intersections = 0 
    for i in range(len(A)):
        newArr.append((i-A[i]))
    newArr.sort()
    
    i = 0 
    j = 0 
    while i < len(newArr) and j < len(A):
        if newArr[i]< A[j]:
            opendiscs +=1
            i+=1 
        elif    




discs([1,5,2,1,4,0])        