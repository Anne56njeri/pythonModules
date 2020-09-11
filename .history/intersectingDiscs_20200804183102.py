def discs(A):
    newArr = []
    for i in range(len(A)):
        newArr.append((i-A[i]))
    newArr.sort()
discs([1,5,2,1,4,0])        