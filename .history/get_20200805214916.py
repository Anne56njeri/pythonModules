def produce(num1,num2):
    totalValue = 0 
    
    for i in range(abs(num1)):
       
        totalValue +=num2 
       
    if abs(num2) > num1:
        return totalValue

print(produce(-2,3))
#  4513 = 4 * 5 * 1 * 3
