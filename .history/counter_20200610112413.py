import math

def numbers(param):
    # takes in a number 
    # returns the number of times the number will be multiplies 
     
    param = str(param)
    answer = 1
    for i in range(len(param)):
        answer *= int(param[i])

    param = str(answer)
    print(param)
        
        
        


numbers(39)    