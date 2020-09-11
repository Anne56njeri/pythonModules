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
            j = len(newStr)-1
            while j >= 0:
                if int(newStr[j]) == 0:
                    break 
                elif int(newStr) % int(newStr[j]) !=0:
                    break 
                
                    newArr.append(int(newStr))
                


                   
                          
    print(newArr)
dividing(1,22)        