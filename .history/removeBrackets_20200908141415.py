def remove(str):
    #  loop from the middle 
    # add both to a stack 
    # whichever stack is not empty return its length 
    stackA = []
    stackB = []
    for i in range(len(str)//2):
        stackA.append(str[i])
    for i in range(len(str),len(str)//2,-1):
        print(str[i])   

remove("(()(")                