from bisect import b
def discs(A):
    start = [i-j for i,j in enumerate(A)]
    start.sort()
    pairs = 0
    for i in range(len(A)):
        end = i +A[i]
        count    





discs([1,5,2,1,4,0])        