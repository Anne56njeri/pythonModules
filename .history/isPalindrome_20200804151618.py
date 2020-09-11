def palindrome(str):
    i = 0 
    j = len(str)-1 
    while i < len(str) // 2 and j >= len(str) // 2:
        i +=1 
        j -=1 

palindrome("hellosannasmith")    