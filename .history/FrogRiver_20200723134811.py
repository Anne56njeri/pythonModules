def Frog(X,A):
    # given x where the frog wants to go
    # find earliest time 
    # once you get the second that has that position
    # return the second 
    pos = set()
    for i in range(len(A)):
        pos.add(A[i])
        if len(pos) == X:
            return i
      

print(Frog(5,[1,1,1,9,2,3,5,4]))        
