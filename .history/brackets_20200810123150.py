def brackets(S):
    # "{[()()]}"
    if len(S) == 0:
        return 1 
    if len(S) % 2 == 1:
        return 0 
    matched = {"]":"[","}":"{",")":"("}
    found = ["[","(","{"]
    opening = []

    for i in S:
        if i in found:
            opening.append(i)
        else:
            if len(opening) == 0:
                return 0 
    for i in range(len(S) //2,len(S)):
        if S[i] in matched:
          if matched[S[i]] == opening[-1]:
              opening.pop()
    if len(opening) == 0:
        return 1
    return 0                          
                

        


       
print(brackets("[{()}]"))                          

