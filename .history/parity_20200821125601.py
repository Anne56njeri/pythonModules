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
    return even + odd            
# using list comprehension
def sol(A):
    return ([item for item in A if item % 2 == 0 ] + [item for item in A if item %2 ==1])
print(sol([3,1,2,4]))
# 