import math 

def solution(A,B,K):
    # find the number of numbers that  are divisible by k 
    # take the time complexity of 0(n)
    # brute force 
    count = (B-A) +1 
    if K % 2 == 0:
        print(ans)
    answer = math.ceil(count / K)
    print(answer)

# solution(6,12,3)          
solution(1,10,4)    