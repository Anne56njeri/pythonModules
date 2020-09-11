import math 

def solution(A,B,K):
    # find the number of numbers that  are divisible by k 
    # take the time complexity of 0(n)
    # brute force 
    return (B - A) // K +1

# solution(6,12,3)          
print(solution(6,11,1))  