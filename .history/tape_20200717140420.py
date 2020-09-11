def tape(A):
    # goal is to find minimal abs difference  
    # so its i - i:len(A)
    i = 0 
    diff = []
    while i < len(A)-1:
        print(A[i+1:len(A)])
        i+=1


tape([3,1,2,4,3])    