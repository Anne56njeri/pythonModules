def product(num):
    result = []
    # this loop is running from highest to lowest 
    # numbers = range(num,0,-1)
    
    for i in range(num,0,-1):
        if(num // i) * i == num:
            print('well',len(num // i , i))
            result.append(len("%s%s" %(str(num // i),str(i))))
            # print('result',result)
product(8)        