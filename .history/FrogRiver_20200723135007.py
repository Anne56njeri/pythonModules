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
            
      

print(Frog(2,[2]))        
