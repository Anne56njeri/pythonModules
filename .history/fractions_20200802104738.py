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
    # create a map to store already seen remainders 
    # remainder is used as key and its position in result is stored as value 
    # position for cases like 1/6
    mp = {}

    # find the first remainder 
    rem = numerator / denominator
    print(rem)
    # keep finding the remainder until the remainder becomes 0 or repeates 
   while rem !=0 and rem in mp:
       mp[rem] = len(res)
       rem = rem * 10 
       # append the rem / denomintor to result 
       res_part = rem / denominator 
       res += str(res_part)
       # update the remainder 
       rem = 
   

    
print(frac(4,333))   