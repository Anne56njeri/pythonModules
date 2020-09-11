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
# Time complexity  o(n)
# space complexity o(1)
def solution(A):
    # you have two pointers start and end 
    # increment start till we find an odd element 
    # if we encounter an odd element then we'll decrement the end pointer 
    # we decrement the end element  index until we find an even number then swap them 
    start = 0 
    end = len(A) -1 
    while start < end:
        if A[start] % 2 == 0:
            start +=1
        else:
            if A[end] %2 == 0:
                

        