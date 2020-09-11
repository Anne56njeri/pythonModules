def produce(num1,num2):
    totalValue = 0 
    for i in range(abs(num1)):
        print(i)
        totalValue +=num2 
    if num1 < 0 and num2 > 0:
        str = str(totalValue)
        newStr = "-" + str 
        print(i)    
    print(totalValue)  

produce(-2,3)
#  4513 = 4 * 5 * 1 * 3
