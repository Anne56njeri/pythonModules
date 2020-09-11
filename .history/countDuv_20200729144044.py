import math 

def solution(A,B,K):
    # find the number of numbers that  are divisible by k 
    # take the time complexity of 0(n)
    # brute force 
    count = (B-A) + 1
    if K % 2 == 0:
        answer =  count // K
        return answer
    else:    
        answer = math.ceil(count / K)
        return answer

# solution(6,12,3)          
print(solution(1,11,1))  