def repeated(s):
    # soo umm we supposed to check if the string can be
    # made from its substring 
    if len(s) == 0:
        return False
    n = len(s)
    for i in range(n// 2,0,-1):
        print('i',i)
        newStr = s[0:i]
        print(newStr)
        count = 1 
        while len(newStr) <= n:
            newStr = s[0:i] * count 
            if newStr == s:
                
                return True
            
            count +=1  
    return False              
        


    
print(repeated("abcabcd"))    