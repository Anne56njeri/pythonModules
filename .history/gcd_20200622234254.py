def gcd(a,b):
    while (b !=0):
        t = a
        a = b 
        b = t %b 
    return a   

gcd(20,)     