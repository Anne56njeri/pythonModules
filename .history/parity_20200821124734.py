def parity(A):
    # we can have two arrays one to store even and other to store odd 
    # that would cost memory 
    even = []
    odd = []
    for i in range(len(A)):
        if A[i]%2 == 0:
            even.append(A[i])
        else:
            odd.append(A[i])
                


parity([3,1,2,4])