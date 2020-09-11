import json 

def dividing(upper,lower):
    newArr = []
    numbers = range(upper,lower+1)
    for i in numbers:
        if i > 0 and i < 10:
            newArr.append(i)
        
        else:
            
            #  we want to loop only if the length is greater than one 
            if selfDiv(i):
                newArr.append(i) 
    print(newArr)            

def selfDiv(num):
    newStr = str(num)

    for i in newStr:
        if int(i) == 0:
            return False
        elif int(newStr) % int(i) !=0:
            return False 
    return True                        


                   
     
dividing(1,22)        