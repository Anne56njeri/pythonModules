import math 

def solution(A,B,K):
    # find the number of numbers that  are divisible by k 
    # take the time complexity of 0(n)
    # brute force 
    count = (B-A) +1 
    print(count // K )

solution(6,12,2)          
# solution(0,2000000000,10)    