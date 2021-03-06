def counter(N,A):
    # we are going to create a counts array that gets to N
    # we are going to increment by 1 if we come across any 
    # number in the A ---> array 
    # when we get to a number that is greater(out of range)
    # we've maxed out and at this point all counters are set to the max value 
    # then we continue with the operation 
    counts = [0] * N 
    counterIndex = 0
    for i in range(len(A)):
        if A[i] <= N:
            counts[A[i]-1] +=1 
            if counts[A[i]-1] > counterIndex:
                counterIndex = counts[A[i]-1]
        else:
            print('counts',counterIndex)
            
            counts = [counterIndex] *N
            
    return counts    
# print(counter(5,[3,4,4,6,1,4,4,]))         
def maxC(N,A):
    counters = [0] * N 
    max_1 = 0 
    max_2 = 0 
    for x in A:
        if x <=N:
            if max_1 > counters[x-1]:
                counters[x-1] = max_1 
            counters[x-1] +=1 
            if max_2 < counters[x-1]:
                max_2 = counters[x-1]
        else:
            
            max_1 = max_2 
    counters = [max(max_1,i) for i in counters]
    return counters                                            

print(maxC(5,[3,4,4,6,1,4,4,]))    