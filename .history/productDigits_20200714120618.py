def product(num):
    result = []
    # this loop is running from highest to lowest 
    numbers = range(0,num)
    for j in numbers:
        print(j)
    for i in range(num,0,-1):
        print(i)
product(8)        