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
    res = ""
    if numerator == 0:
        return "0"
    if denominator == 0:
        return "undefined"    
    if (numerator < 0 and denominator > 0) or (numerator > 0 and denominator <0):
        res += "-" 
        numerator = abs(numerator)
        denominator = abs(denominator)
    if numerator % denominator == 0:
        return str(numerator // denominator)
    else:
        #  this means its has a remainder 
        res += str(numerator // denominator)
        res += "."  
    newDict = {}
    rem =  numerator %  denominator
    
    while rem != 0:
        
        if rem in newDict:
            position = res.find(str(rem // de)) + 1
            print(position)
            # res = res[:position] + "(" + res[position:] + ')'
            

            break 
        newDict[rem] = len(res)
        rem *=10 
        res_part = rem // denominator
        res += str(res_part)
        rem = rem % denominator
    return res 
    


      
    
   

    
print(frac(1,6))   