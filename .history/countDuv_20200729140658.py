def solution(A,B,K):
    # find the number of numbers that  are divisible by k 
    # take the time complexity of 0(n)
    # brute force 
    count = 0 
    for i in range(A,B+1):
        print(i)
        if i % K == 0:
            count +=1 
    print('count',count)        
(6,11,2)    