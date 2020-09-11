import re 

def palindrome(str):
    if len(str) == 0:
        return True 
    
    str = str.lower()
    cleanStr = re.sub(r"[,:.;:@#?!&$]+",' ',str)
    
    cleanStr = cleanStr.split(" ")
    cleanStr.reverse()
    newArr = []
   
    for i in cleanStr:
        newArr.append(i[::-1])
    print("".join(newArr))    

palindrome("A man, a plan, a canal: Panama")
