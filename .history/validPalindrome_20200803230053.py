import re 

def palindrome(str):
    if len(str) == 0:
        return True 
    actualStr = str.lower()
    str = str.lower()
    cleanStr = re.sub(r"[,.;@#?!&$]+",' ',str)
    print('cleanStr',cleanStr)
    str = str.split(" ")
    str.reverse()
    newArr = []
    print(actualStr)
    for i in str:
        newArr.append(i[::-1])
    print(newArr)    

palindrome("A man, a plan, a canal: Panama")
