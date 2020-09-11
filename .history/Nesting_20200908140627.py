def nesting(S):
    # move them to a stack 
    # then check and make sure they are not equal
    # if the are 
    # return 0 
    # else return 1 
    if len(S) == 0:
        return 1
    stackA = []
    stackB = []
    for i in S:
        if i == "(":
            stackA.append(i)
        elif i == ")":
            stackB.append(i)   
    if len(stackA) != len(stackB):
        return 0 
    else:
        print(stackA)
        print(stackB)
        while stackA !=[] and stackB !=[]:
            if stackA.pop()  == stackB.pop():
                return 0 
        return 1            
   
               

print(nesting("(()"))      