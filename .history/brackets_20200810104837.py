def brackets(str):
    # "{[()()]}"
    if len(str) == 0:
        return 1 
    countSopen = 0 
    countCopen = 0 
    countBopen = 0 
    for i in str:
        if i == "{":
            countCopen +=1 
        elif i == "[":
            countSopen +=1 
        elif i == "(":
            countBopen +=1 
        elif (i == "}" and countCopen == 0) or (i == ")" and countBopen == 0) or (i == "]" and countSopen == 0):
            return 0 
        elif i =="}":
            countCopen -=1 
        elif i == "]":
            countSopen -=1 
        elif i == ")":
            countBopen -=1       
    if countBopen == 0 and countCopen == 0 and countSopen == 0:
        return 1 
    return 0 
print(brackets("{[()()]}"))                          

