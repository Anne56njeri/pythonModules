def fractions(numerator,denominator):
    if denominator == 0 :
        return str(nu)
    number = numerator / denominator
    newStr = str(number)
    
    largeStr = newStr.split(".")
    if len(largeStr[1]) > 1:
        return largeStr[0] + "." +  '(' + largeStr[1][0] + ')' 
    return newStr
        

   

    
print(fractions(1,0))   