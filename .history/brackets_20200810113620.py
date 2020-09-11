def brackets(S):
    # "{[()()]}"
    if len(S) == 0:
        return 1 
    countS = 0 
    countB = 0 
    countC = 0 
    for i in S:
        if i == "(" and stack[-1] == ")":
            stack.pop()
            
        

    
        
print(brackets("([)()]"))                          

