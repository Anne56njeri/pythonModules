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
#  lets use recursion  
def product(num1,num2):
    # when you have num2 as a negative 
    if num2 < 0 :
        print('h')
        print('num2',num2)
        return -product(num1,-num2)
    if num1 == 0 or num2 == 0:
        return 0
    if num2 == 1:
        print('num1',num1,'num2',num2)
        return num1 
    else:
        return num1 + product(num1,num2-1)    
    
print(product(2,-3))   

def product1(x,y):
    answer = x/(1/y)
    print(answer)
# product1(2,3)    
# using a while loop 
def mult(a,b):
    if a == 0 or b == 0:
        return 0 
    
    result = 0 
    value = abs(b) 
    while value > 0:
        result +=abs(a)
        value -=1 
    if (b < 0 and a > 0 ) or   (b > 0 or a  < 0):
        num = str(result)
        num =  "-" + num 
        return int(num)
    else:
        return result
# print(mult(2,-3))            
def bitwise(a,b):
    # runs till  b is 0
    result = 0 
    while b:


