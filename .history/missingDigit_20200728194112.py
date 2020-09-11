def missing(s):
    s = s.replace("=","==")
    for  x in range(1000000):
        try:
            if eval(s.replace("x",str(x))):
                return x 
        except:
            pass 
    return             

    print(s)
missing("3x + 12 = 46")    