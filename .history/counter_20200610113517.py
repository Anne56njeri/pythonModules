import math

def numbers(param):
    # takes in a number 
    # returns the number of times the number will be multiplies 
     
    param = str(param)
    answer = 1
    i = 0
    count = 0 
    while i < len(param):
        answer *= int(param[i])
        param = str(answer)
        if answer >10:
            count +=1
        else:

            return count    


    
        
        
        


numbers(39)    