import re 

def palindrome(str):
    if len(str) == 0:
        return True 
    
    str = str.lower()
    cleanStr = re.sub(r"[,:.;:@#?!&$]+",' ',str)
    
    actualStr = cleanStr.split(" ")
    actualStr.reverse()
    newArr = []
    finalArr = []

    for i in actualStr:
        newArr.append(i[::-1])
    for i in newArr    
    print(cleanStr)    
    print(newArr)    

palindrome("A man, a plan, a canal: Panama")
