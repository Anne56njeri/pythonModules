def palindrome(str):
    if len(str) == 0:
        return True 

    str = str.lower()
    
    str = str.split(" ")
    str.reverse()
    newArr = []
    print(str)
    for i in str:
        newArr.append(i[::-1])
    print(newArr)    

palindrome("A man, a plan, a canal: Panama")
