def missing(s):
    s = s.replace("=","==")
    for  x in range(1000000):
        try:
            if eval(s.replace("x",str(x))):
                print(s.replace)
                return x 
        except:
            pass 
    return None            

    print(s)
missing("3x + 12 = 46")    