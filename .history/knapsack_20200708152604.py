def Knap(a,b,w):
    # declare an empty dictionary 
    newArr = []
    for i,j in zip(a,b):
        smallArr = []
        smallArr.append(i)
        smallArr.append(j)
        newArr.append(smallArr)
    

    print(newArr)
        

Knap([10,20,30],[60,100,120],220)    