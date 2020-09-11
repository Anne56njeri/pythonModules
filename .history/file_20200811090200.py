# a,b --> 2*3 == 2 + 2 + 2 = 6 
# use for loop or a while loop 
# 
def product(a,b):
    if a == 0 or b == 0:
        return 0

    total = 0 
    btimes = abs(b)
    while btimes > 0:
        total +=abs(a)
        btimes -=1 
    if b < 0 and a > 0:
        number = str(total)
        number = "-" + number
        return number 
    elif b        


        
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