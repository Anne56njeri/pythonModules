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
            if selfDiv(i):
                newArr.append(i)

def selfDiv(num):
    newStr = str(num)

    for i in newStr:
        if int(newStr) % int(i) !=0:
            return False 
    return True                        


                   
                          
    print(newArr)
dividing(1,22)        