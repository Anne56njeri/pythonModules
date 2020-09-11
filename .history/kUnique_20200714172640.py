def unique(str):
    # getting th number of unique char 
    
    print('len',len(str))
    newArr = []
    for i in range(num,len(str) + 1):
        print('i-',i)
        for j in range(1,i):
            print('j-->',j)

unique("2aabbacbaa")        