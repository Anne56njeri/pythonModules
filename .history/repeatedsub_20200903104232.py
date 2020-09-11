def rep(s):
    if len(s) == 0:
        return False 
    n = len(s)
    for i in range(n // 2,0,-1):
        string = s[0:i]
        count = 1 
        newString = string * count
        while len(newString) <=n:
            if newString == s:
                return True 
                    

