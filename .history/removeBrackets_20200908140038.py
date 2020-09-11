def remove(str):
    # find how many make a complete pair 
    # subtract that from the total 
    total = len(str)
    complete = 0
    opening = 0
    closing =  0
    for i in range(len(str)):
        if str[i] == "(":
            opening +=1 
        else:
            closing +=1 
    print(clos)        
remove("(()(")                