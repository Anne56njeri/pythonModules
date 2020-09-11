def counting(A,m):
    n = len(A)
    count = [0] * ( m +1 )
    for k in range(n):
        count[A[k]] +=1
    print()    
    return count 

print(counting([1,2,2,4,5,5],6))      