def palindrome(str):
    if len(str) == 0:
        return True 

    str = str.lower()
    str.reverse()
    str = str.split(" ")
    newArr = []
    print(str)
    for i in str:
        print(i[::-1])

palindrome("A man, a plan, a canal: Panama")
