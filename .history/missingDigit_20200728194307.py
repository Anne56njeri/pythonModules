def missing(s):
    s = s.replace("=","==")
    for  x in range(10):
        try:
            # what shall we replace with that 
            # currently equal
            if eval(s.replace("x",str(x))):
                print('here',s.replace("x",str(x)))
                return x 
        except:
            pass 
    return None            

    
missing("4 + 2 = x")    