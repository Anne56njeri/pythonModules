def string(str):
    st = list(str)
    count = 0 
    while count < 10:
        for i in range(0,len(st)-1):
            pair = st[i] + st[i+1]
            print(pair)
        count +=1    


string("abcabc")    