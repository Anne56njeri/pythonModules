import math

def numbers(param):
    # takes in a number 
    # returns the number of times the number will be multiplies 
     
    param = str(param)
    answer = 1
    for i in range(len(param)):
        answer = math.prod(int(param[i]))
        print(answer)
        
        


numbers(39)    