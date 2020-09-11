import math 

def solution(A,B,K):
    # find the number of numbers that  are divisible by k 
    # take the time complexity of 0(n)
    # brute force 
    count = (B-A) +1 
    answer = math.ceil(count / K)
    print(answer)

# solution(6,12,3)          
solution(0,100,2)    