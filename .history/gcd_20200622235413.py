def gcd(a,b):
     # a = 20
     #b = 8 
     # a % b = 4 , new a = previous b which is 8 and b = r
    r = b #8 
    while r != 0:
        r = a % b 
        a = b # 8
        b = r # 4
        print('b',b)
    return b    

    # while b !=0:
    #     # t = a
    #     b = a % b # 4
    #     a = b 
        
    #     print('b',b)
    #     print('a',a)
    # return b  

print(gcd(20,8)) #where a >b ,when b !=0 then b = a%b, then re assign a = b ,b = a%b    