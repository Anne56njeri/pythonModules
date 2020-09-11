def fractions(numerator,denominator):
    if denominator == 0 :
        return str(numerator)

    number = numerator / denominator
    if numerator % denominator == 0:
        return str(numerator // denominator)
    newStr = str(number)
    print(newStr)
    largeStr = newStr.split(".")

    if len(largeStr[1]) > 1:
        return largeStr[0] + "." +  '(' + largeStr[1][0] + ')' 
     
    return newStr
        
def frac(numerator,denominator):
    res = []
    if numerator == 0:
        return "0"
    if denominator == 0:
        return "undefined"    
    if numerator / denominator < 0:
        print('here')
        res.append("-")
        
    numerator = abs(numerator)
    denominator = abs(denominator)
    if numerator % denominator == 0:
        return "".join(res
    else:
        #  this means its has a remainder 
        res.append(str(numerator // denominator))
        res.append(".")  
    newDict = {}
    rem =  numerator %  denominator
    
    while rem != 0:
        # print(newDict)

        if rem in newDict:
            print('rem',rem)
            res.insert(newDict[rem],"(")
            res.append(")")
           
            

            break 
        newDict[rem] = len(res)
        rem *=10 
        res_part = rem // denominator
        res .append(str(res_part))
        rem = rem % denominator
    print(res)    
    return "".join(res)
    


      
    
   

    
print(frac(-21474836481,1))   