def produce(num1,num2):
    totalValue = 0 
    
    for i in range(abs(num1)):
       
        totalValue +=abs(num2)
       
    print(totalValue)
    if num1 < 0 and num2 > 0:
        str1 = str(totalValue)
        newStr = "-"+ str1 
        return int(newStr)
    elif num1 > 0 and num2 < 0:
        str1 = str(totalValue)
        newStr = "-"+ str1 
        return int(newStr)
    else:
        return     


print(produce(-2,3))
#  4513 = 4 * 5 * 1 * 3
