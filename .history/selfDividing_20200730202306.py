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
            selfDiv(newStr)
                


                   
                          
    print(newArr)
dividing(1,22)        