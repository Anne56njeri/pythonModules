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
        if i == len(newArr)- 1:
            break
        if newArr[i]<=A[j]:
            opendiscs +=1
            if opendiscs > 1:
                intersections +=opendiscs
            i+=1 
        elif newArr[i] > A[j]:
            opendiscs -=1 
            j+=1   
    re       





discs([1,5,2,1,4,0])        