def remove(str):
    #  loop from the middle 
    # add both to a stack 
    # whichever stack is not empty return its length 
    stackA = []
    stackB = []
    for i in range(len(str)//2):
        stackA.append(str[i])
    for i in range(len(str),0,-1):
        print(i)   

remove("(()(")                