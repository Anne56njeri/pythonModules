# given an array rotate it k times to the right 
def rotate(A,K):
    # first I'd rotate the array once 
    # so how do we rotate the array 
    # we move the last element to the firs place and
    # the rest follow suit 
    # moving elements to the right in an array 
    # [3,8,9,7,6]
    # 3 ---> 0 now 3 ---> 1
    # 8 ---> 1 now 8 ---> 2
    #  A[0] = A[len]
    # [6 ,3,8,9,7]
    # what do you notice that   A[i] = A[i+1]
    i = 0 
    for i in range(len(A)-1):
        A[i] = A[i+1]
        if i == len()
           
        


      
rotate([3, 8, 9, 7, 6], 3)    
