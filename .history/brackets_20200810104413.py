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
        if i == "[":
            count    

