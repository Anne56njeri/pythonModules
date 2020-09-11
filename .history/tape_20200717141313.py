def tape(A):
    # goal is to find minimal abs difference  
    # so its i - i:len(A)
    i = 0 
    diff = []
    if A != []:

        while i < len(A)-1:
            # print('i',sum(A[:i+1]),'sum',sum(A[i+1:len(A)]))
            total = sum(A[:i+1]) - sum(A[i+1:len(A)])
            diff.append(abs(total))
            
            i+=1
        return min(diff) 
    else:
        return 1      


print(tape([3,1,2,4,3]))   