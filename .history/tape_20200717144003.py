def tape(A):
    # goal is to find minimal abs difference  
    # so its i - i:len(A)
    i = 0 
    min_diff = abs(A[0] - sum(A[1:]))
    print('min',min_diff)
    if A != []:

        while i < len(A)-1:
            print('i',sum(A[:i+1]),'sum',sum(A[i+1:len(A)]))
            total = sum(A[:i+1]) - sum(A[i+1:len(A)])
            print('t',abs(total))
            
            
            i+=1
        
    else:
        return 1     

tape([3,1,2,4,3])
def tapeE(A):
    head = A[0]
    tail = sum(A[1:])
    min_diff = abs(head - tail)
    for index in range(1,len(A)-1):
        head +=A[index]
        tail -= A[index]
        print('head',head)
        if abs(head - tail) < min_diff:
            min_diff = abs(head - tail)
        return min_diff    
# print(tapeE([3,1,2,4,3]))