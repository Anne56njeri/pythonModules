def string(str):
    st = list(str)
    count = 0 
    while count < 500:
        for i in range(len(st)-1,2):
            pair = st[i] + st[i+1]
            print(pair)
        count +=1    


string("abcabc")    