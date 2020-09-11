def gcd(a,b):
    while (b !=0):
        # t = a
        # a = b 
        b = a %b 
    return a   

gcd(20,8) #where a >b ,when b !=0 then b = a%b     