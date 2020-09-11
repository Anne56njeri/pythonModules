def brackets(S):
    # "{[()()]}"
    stack = []
    for i in S:
        stack.append(i)
    for i in S:
        if ( i == "(" and stack.pop() != ")") or (i == "{" and stack.pop())       

print(brackets("{[()()]}"))                          

