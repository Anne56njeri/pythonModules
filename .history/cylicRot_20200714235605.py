# given an array rotate it k times to the right 
def rotate(A,K):
    # first I'd rotate the array once 
    # so how do we rotate the array 
    # we move the last element to the firs place and
    # the rest follow suit 
    # moving elements to the right in an array 
    # [3,8,9,7,6]
    # [6,3,8,9,7]
    for i in range(len(A)-1):
        A[i] = A[len(A)-1]
        A[len(A)-1] = A[len(A)-2]
        A[i] = A[i+1]
        print(A)


      
rotate([3, 8, 9, 7, 6], 3)    
