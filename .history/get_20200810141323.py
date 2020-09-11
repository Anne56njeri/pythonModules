def produce(num1,num2):
    totalValue = 0 
    
    for i in range(abs(num1)):
       
        totalValue +=abs(num2)
    
    if num1 < 0 and num2 > 0:
        str1 = str(totalValue)
        newStr = "-"+ str1 
        return int(newStr)
    elif num1 > 0 and num2 < 0:
        str1 = str(totalValue)
        newStr = "-"+ str1 
        return int(newStr)
    else:
        return totalValue    


# print(produce(2,3))
def findProduct(num):
    str1 = str(num)
    totalValue = 1
    for i in str1:
        totalValue *=int(i)
    print(totalValue)
      
#  4513 = 4 * 5 * 1 * 3
# A similar way 
def getProduct(n):
    product = 1 

    while n != 0:
        product *= n %10 
        n = n // 10 
    print(product)   
getProduct(4513)   
def product(num1,num2):
    if num2 < 0:
        return -product(num1,-num2)
    elif y == 0:
