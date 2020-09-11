def palindrome(str):
    if len(str) == 0:
        return True 

    str = str.lower()
    str = str.split()
    newArr = []
    for i in str:
        newArr.append(i[::-1])
    newStr = "".join(newArr)   

    
    print("".join(str))

palindrome("A man, a plan, a canal: Panama")
