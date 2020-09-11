# a,b --> 2*3 == 2 + 2 + 2 = 6 
# use for loop or a while loop 
# 217856 = 2*1*7*8*5*6

import sys
def product(a,b):
    # print('number',sys.maxsize)
    if a == 0 or b == 0:return 0

    total = 0 
    if a > b:
        smaller = abs(b) 
        greater = abs(a)
    else:
        greater = abs(b)
        smaller = abs(a)    

    while smaller > 0:
        total +=greater]
        btimes -=1 
    if (b < 0 and a > 0) or (b > 0 and a < 0):
        return -(total) 
   
    return total

print(product(-2,3))  
print("========")
print(product(2,-3))  
print("========")    
print(product(-2,-3))
print("========") 
print(product(0,2))
print("========") 
print(product(0,2))
print("========")
print(product(9223372036854775807,10))
