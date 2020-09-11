def brackets(S):
    # "{[()()]}"
    '''
    { ---> added to stack 
    [ ---> added to stack 
    ( ----> added to stack 
    at this point we come across a closing bracket 
    our stack looks like this 
    )
    [
    { 
    therefore we shall match  it with the first closing bracket we come across 
    # in this case they match we pop it right 
    
        '''
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
            #  otherwise the length is not 0 then we check if that closing brackets matches with the one in the stack. first in last out 
            
            elif matched[i] == opening[-1]:
                opening.pop()
                                
    if len(opening) == 0:
        return 1
    return 0            
   
print(brackets("v"))                          

