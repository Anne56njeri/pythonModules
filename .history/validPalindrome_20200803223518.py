def palindrome(str):
    if len(str) == 0:
        return True 

    str = str.lower()
    str = str.split(",")
    newArr = []
    for i in str:
        newArr.append(i[::-1])
    newStr = "".join(newArr)
    secondStr = "".join(str)   
    print('first',secondStr,'sec',newStr)

palindrome("A man, a plan, a canal: Panama")
