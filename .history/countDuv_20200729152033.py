import math 

def solution(A,B,K):
    # find the number of numbers that  are divisible by k 
    # take the time complexity of 0(n)
    # brute force 
    if A % K == 0:
        return (B - A) // K +1
    if A % K > 0:
        return (B -)    

# solution(6,12,3)          
print(solution(10,10,5))  