def discs(A):
    newArr = []
    for i in range(len(A)):
        newArr.append((i-A[i]))
    print(newArr)
discs([1,5,2,1,4,0])        