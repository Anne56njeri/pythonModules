def palindrome(str):
    if len(str) == 0:
        return True 
        
    str = str.lower()
    str = str.split()
    str.reverse()
    
    print(str)

palindrome("A man, a plan, a canal: Panama")
