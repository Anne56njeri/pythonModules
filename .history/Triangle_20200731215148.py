def triangle(A):
    A.sort()
    for i in range(len(A)-2):
        p = A[i]
        q = A[i+1]
        r = A[i+2]
        print('p',p,'q',q,'r',r)
triangle([10,])        