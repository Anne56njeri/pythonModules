def unique(str):
    # getting th number of unique char 
    num = int(str[0])
   
    newArr = []
    for i in range(num,len(str) + 1):
        print('i-------->',i)
        for j in range(1,i):
            print('j-->',j)
            if len(set(string[j:i]) == num):
                newArr.append(string[j:i])

unique("2aabbacbaa")        