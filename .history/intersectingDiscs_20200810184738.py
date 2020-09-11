from bisect import bisect_right
def discs(A):
    start = [i-j for i,j in enumerate(A)]
    start.sort()
    pairs = 0
    for i in range(len(A)):
        end = i +A[i]
        count  = bisect_right(start)  





discs([1,5,2,1,4,0])        