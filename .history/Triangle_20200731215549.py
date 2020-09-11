def triangle(A):
    A.sort()
    for i in range(len(A)-2):
        p = A[i]
        q = A[i+1]
        r = A[i+2]
        print('p',p,'q',q,'r',r)
        if (p + q) > r and (q + r) > p and (r + p) > q:
            return 1
            
    return 0 
                   
print(triangle([10,2,5,1,8,20]))        