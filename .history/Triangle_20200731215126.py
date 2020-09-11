def triangle(A):
    A.sort()
    for i in range(len(A)):
        p = A[i]
        q = A[i+1]
        r = A[i+2]
        print('p',p,'')
        