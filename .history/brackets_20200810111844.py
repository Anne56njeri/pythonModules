def brackets(S):
    # "{[()()]}"
    if len(S) == 0:
        return 1 
    countS = 0 
    countB = 0 
    countC = 0 
    for i in S:
        if i == "(":
            countB +=1 
        elif i == "[":
            countS +=1 
        elif i == "{":
            countC += 1  
        elif (i == ")" and countB == 0) or (i == " }" and countC == 0 ) or (i =):              
    
        
print(brackets("([)()]"))                          

