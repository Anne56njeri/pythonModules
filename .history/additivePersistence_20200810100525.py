def add(num):
    # convert number to string format
    num = str(num)
    count = 0 
    while len(num) > 1:
        sum = 0 
        for i in num:
            sum +=int(i)