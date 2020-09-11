def missing(s):
    s = s.replace("=","==")
    for  x in range(10):
        try:
            if eval(s.replace("x",str(x))):
                print('here',s.replace("x",str(x)))
                return x 
        except:
            pass 
    return None            

    
missing(" + 12 = 46")    