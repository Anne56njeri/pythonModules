def remove(str):
    #  loop from the middle 
    # add both to a stack 
    # whichever stack is not empty return its length 
    stackA = []
    stackB = []
    n = len(str)
    for i in range((len(str)//2)-1):
        print(i)
        stackA.append(str[i])
    


remove("(()(")                