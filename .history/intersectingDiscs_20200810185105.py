from bisect import bisect_right
def discs(A):
    start = [i-j for i,j in enumerate(A)]
    start.sort()
    
    newArr = []
    for i in range(len(A)):
        count = 0
        for j in range(len(start)):
            if A[i] > start[j]:
                count +=1 
        newArr.append(count-1)
    for i in range(len(newArr)):
        newArr[i] = newArr[i] - i 
    print(newArr[i])              
        





discs([1,5,2,1,4,0])        