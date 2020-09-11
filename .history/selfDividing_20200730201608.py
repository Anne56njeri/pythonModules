import json 

def dividing(upper,lower):
    newArr = []
    numbers = range(upper,lower+1)
    for i in numbers:
        if i > 0 and i < 10:
            newArr.append(i)
        
        else:
            newStr = str(i)
            #  we want to loop only if the length is greater than one 
            j = 0 
            while j < len(newStr):
                if int(newStr[j]) == 0:
                    break 
                elif int(newStr)
                j +=1


                   
                          
    print(newArr)
dividing(1,22)        