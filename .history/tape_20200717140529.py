def tape(A):
    # goal is to find minimal abs difference  
    # so its i - i:len(A)
    i = 0 
    diff = []
    while i < len(A)-1:
        total = i - 
        diff.append(abs(i-sum(A[i+1:len(A)])))
        
        i+=1
    print(diff)    


tape([3,1,2,4,3])    