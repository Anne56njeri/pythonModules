def add(num):
    # convert number to string format
    num = str(num)
    count = 0 
    while len(num) > 1:
        total = 0 
        for i in num:
            sum +=int(i)
        count +=1 
        num = str(total)     