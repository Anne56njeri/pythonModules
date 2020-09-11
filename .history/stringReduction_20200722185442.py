def string(str):
    st = list(str)
    count = 0 
    while count < 1000:
        for i in range(len(st)-1):
            pair = st[i] + st[i+1]
            print(pair)
        count    


string("abcabc")    