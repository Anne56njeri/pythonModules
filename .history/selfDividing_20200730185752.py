import json 

def dividing(upper,lower):
    newArr = []
    numbers = range(upper,lower+1)
    for i in numbers:
        if i > 0 and i < 10:
            newArr.append(i)
        elif i % 10 == 0:  
            continue
        else:
            newStr = json.dumps(i)
            if len(newStr) > 1:
                for i in newStr:
                    if i != '0':

                        if int(newStr) % int(i) == 0:
                            newArr.append(int(newStr))  
                        else:
                            break 
                    else:
                        break       
    print(newArr)
dividing(1,22)        