def brackets(S):
    # "{[()()]}"
    stack = []
    for i in S:
        stack.append(i)

print(brackets("([)()]"))                          

