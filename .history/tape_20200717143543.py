def tape(A):
    # goal is to find minimal abs difference  
    # so its i - i:len(A)
    i = 0 
    min_diff = 
    if A != []:

        while i < len(A)-1:
            print('i',sum(A[:i+1]),'sum',sum(A[i+1:len(A)]))
            total = sum(A[:i+1]) - sum(A[i+1:len(A)])
            diff.append(abs(total))
            
            i+=1
        
    else:
        return 1     


print(tape([]))   
def tapeE(A):
    head = A[0]
    tail = sum(A[1:])
    min_diff = abs(head - tail)
    for i in range(1,len(A)-1):
        head +=A[index]
        tail -= A[index]
        if abs(head - tail) < min_diff:
            min_diff = abs(head - tail)
        return min_diff    
tape