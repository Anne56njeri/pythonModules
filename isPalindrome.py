def palindrome(str):
    i = 0 
    j = len(str)
    while i <= len(str) // 2 and j >= len(str) // 2:
        print(str[i:j])
        i +=1 
        j -=1 

palindrome("hellosannasmith")    