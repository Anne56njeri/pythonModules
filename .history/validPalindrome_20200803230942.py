import re 

def palindrome(str):
    if len(str) == 0:
        return True 
    if len(str) = 1:
        if str == str[::-1]

    str = str.lower()
    cleanStr = re.sub(r"[,:.;:@#?!&$]+",' ',str)
    
    actualStr = cleanStr.split(" ")
    actualStr.reverse()
    newArr = []
    

    for i in actualStr:
        newArr.append(i[::-1])
    cleanStr = cleanStr.replace(" ","")
    if cleanStr == "".join(newArr):
        return True
    else:
        return False   
      

palindrome("A man, a plan, a canal: Panama")
