def string(str):
    print(len(str) // 2)
    
    for i in range(len(str)//2,0,-1):
        a = str[:i]
        print(a)
        

string("abcababcababcab")    