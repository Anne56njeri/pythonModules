import math 

def solution(A,B,K):
    # find the number of numbers that  are divisible by k 
    # take the time complexity of 0(n)
    # brute force 
    if A % K == 0:
        return (B - A) // K +1
    if A % K > 0:
        return (B - (A - A %K)) // K    

# solution(6,12,3)          
print(solution(5,11,2))  
# Improved solution 
# Find the digits visible by k from 1 to B 
# then from this exclude integers from 1 to A-1 divisible by K 
def sol(A,B,K):
    # complexity is o(1)
    b = B / K 
    a = 0 
    if A > 0:
        a = (A-1) /K 
    else:
        # if A  == 0  we need to be count 
        # it in because 0 is divisible by any positive number 
        b +=1 
    return b -a     

        