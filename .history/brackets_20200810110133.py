def brackets(S):
    # "{[()()]}"
    stack = []
    for i in S:
        stack.append(i)
    for i in S:
        if ( i == "(" and stack[-1] != ")") or (i == "{" and stack[-1] != "}") or (i == "[" and stack[-1] != "]"):
            return 0 
        else:
            stack.pop()
    return 1                  

print(brackets("()"))                          

