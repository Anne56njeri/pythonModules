def remove(str):
    #  loop from the middle 
    # add both to a stack 
    # whichever stack is not empty return its length 
    stackA = []
    stackB = []
    n = len(str)
    x = n//2
    for i in range(0,n//2):
        
        stackA.append(str[i])
    for i in range(n-1,x-1,-1):
        
        stackB.append(str[i]) 
    print(stackA)   
    print(st) 
    


remove("(()(")                