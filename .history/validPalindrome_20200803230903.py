import re 

def palindrome(str):
    if len(str) == 0:
        return True 
    
    str = str.lower()
    cleanStr = re.sub(r"[,:.;:@#?!&$]+",' ',str)
    
    actualStr = cleanStr.split(" ")
    actualStr.reverse()
    newArr = []
    

    for i in actualStr:
        newArr.append(i[::-1])
    cleanStr = cleanStr.replace(" ","")
    if cleanStr == "".join(newArr):
        print ("true")
    else:
        print("false")    
      

palindrome("A man, a plan, a canal: Panama")
