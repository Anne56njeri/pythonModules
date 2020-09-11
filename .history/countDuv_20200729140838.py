def solution(A,B,K):
    # find the number of numbers that  are divisible by k 
    # take the time complexity of 0(n)
    # brute force 
    count = 0 
    for i in range(A,B+1):
        
        if i % K == 0:
            count +=1 
    print('count',count)        
solution(0,2000000000,10)    