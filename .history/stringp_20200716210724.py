def string(str):
    print(len(str) // 2)
    
    for i in range(len(str)//2,0,-1):
        a = str[:i]
        print(a)
        count = 2
        b =''
        #  since its a substring
        while len(b) < len(str):
            b = a 

string("abcababcababcab")    