import re 

def palindrome(str):
    if len(str) == 0:
        return True 
    actualStr = re.sub()
    str = str.lower()
    cleanStr = re.sub(r"[,:.;:@#?!&$]+",' ',str)
    
    cleanStr = cleanStr.split(" ")
    cleanStr.reverse()
    newArr = []
    print(actualStr)
    for i in cleanStr:
        newArr.append(i[::-1])
    print(newArr)    

palindrome("A man, a plan, a canal: Panama")
