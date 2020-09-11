def Hamming(x,y):
    a = "{0:#b}".format(x) 
    print(a)
    b = bin(y).replace("0b", "")
    print(b)
Hamming(1,4)    