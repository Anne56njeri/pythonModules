def brackets(S):
    # "{[()()]}"
    if len(S) == 0:
        return 1 
    stack = []
    for i in S:
        stack.append(i)
    for i in S:
        if i == "(" and stack[-1] == ")":
            stack.pop()
        elif        

        
        

    
        
print(brackets("([)()]"))                          

