def remove(str):
    #  loop from the middle 
    # add both to a stack 
    # whichever stack is not empty return its length 
    stackA = []
    stackB = []
    for i in str:
        if i == '(':
            stackA.append(i)
        else:
            stackB.append(i)
    print(stackA)
    print(stackB)        
    while stackA !=[] and stackB !=[]:
        if stackB[-1] !=stackA[-1]:
            stackA.pop()
            stackB.pop()
        
    if stackA == []:
        return len(stackA)
    elif stackB == []:
        return len(stackB)    

    


print(remove("(()("))               