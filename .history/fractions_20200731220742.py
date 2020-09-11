def fractions(numerator,denominator):
    number = numerator / denominator
    newStr = str(number)
    newStr = newStr.split(".")
    if len(newStr[1]) > 1:
        return newStr[0] + "." + ""

    print(newStr)

    
fractions(2,3)    