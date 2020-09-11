def Frog(X,A):
    # given x where the frog wants to go
    # find earliest time 
    # once you get the second that has that position
    # return the second 
    pos = set()
    for i in range(len(A)):
        if A[i] <= X:
            pos.add(A[i])
        print(pos)    
        if len(pos) == X:
            return i
    return -1        
    print('not possible')        
      

print(Frog(5,[1,3,1,4,2,3,5,4]))        
