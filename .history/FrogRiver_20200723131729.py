def Frog(X,A):
    # given x where the frog wants to go
    # find earliest time 
    # once you get the second that has that position
    # return the second 
    for i in range(len(A)):
        # print(A[i])
        if A[i] == X:
            return i
        
    return -1    

print(Frog(5,[1,3,1,4,2,3,5,4]))        
