def four (num):
    if num  == 1:
        return True
    if num < 4  and num !=1:
        return False 
    if num == 4:
        return True 
    while num >=1:
        if num % 4 != 0:
            return False 
        num = num // 4 
    return True  
print(four(16))                   