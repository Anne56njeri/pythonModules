def fractions(numerator,denominator):
    number = numerator / denominator
    newStr = str(number)
    largeStr = newStr.split(".")
    if len(largeStr[1]) > 1:
        return newStr[0] + "." + newStr[1][0]
    return newStr
        

   

    
print(fractions(2,3))   