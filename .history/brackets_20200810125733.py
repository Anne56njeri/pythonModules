def brackets(S):
    # "{[()()]}"
    if len(S) == 0:
        return 1 
    if len(S) % 2 == 1:
        return 0 
    matched = {"]":"[","}":"{",")":"("}
    found = ["[","(","{"] 
    opening = []
    # we loop through our string 
    for i in S:
        #  if a bracket is opening we shall add it to a stack
        if i in found:
            opening.append(i)
        else:
            # means we got to a closing bracket,in the case where we did and len(stack) == 0 that means
            # our brackets are not properly nested cause a closing bracket comes first
            if len(opening) == 0:
                return 0 
            #  otherwise 
            elif matched[i] == opening[-1]:
                opening.pop()
                                
    if len(opening) == 0:
        return 1
    return 0            
   
print(brackets("v"))                          

