def string(str):
    print(len(str) // 2)
    print(str[:1] * 2)
    
    # for i in range(len(str)//2,0,-1):
    #     a = str[:i]
    #     print(a)
    #     count = 2
    #     b =''
    #     #  since its a substring
    #     while len(b) < len(str):
    #         b = a * count
    #         print('b',b)
    #         if b == str:
    #             print(a)
    #         count +=1 
    # return -1           

string("abcababcababcab")    