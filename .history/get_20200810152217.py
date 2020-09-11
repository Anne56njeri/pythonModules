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
  
def product(num1,num2):
    if num2 < 0:
        return -product(num1,-num2)
    elif num2 == 0 or num1 == 0:
        return 0 
    elif num2 == 1:
        print('hh')
        
        return  num1
    elif num1 == 1:
        print('h')
        
        
        return num2 
    else:
        print('num1',num1,'num2',num2)
        return num1 + product(num1,num2-1) 
print(product(2,3) )      
def product1(x,y):
    answer = x/(1/y)
    print(answer)
# product1(2,3)    



