def remove(str):
    #  loop from the middle 
    # add both to a stack 
    # whichever stack is not empty return its length 
    stackA = []
    stackB = []
    n = len(str)
    for i in range(0,n//2):
        print(i)
        stackA.append(str[i])
    for i in range(n,n//2,-1):
        print(i)    
    


remove("(()(")                