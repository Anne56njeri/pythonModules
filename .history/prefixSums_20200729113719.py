def prefix(A):
    n = len(A)
    p = [0] * (n+1)
    print(p)
    for k in range(1,n+1):
        p[k] = p[k-1] + A[k-1]
    print(p)    