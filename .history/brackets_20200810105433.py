def brackets(S):
    # "{[()()]}"
    stack = []
    for i in S:
        stack.append(i)
    for i in S:
        if i == stack.pop():
            return 0 
             

print(brackets("([)()]"))                          

