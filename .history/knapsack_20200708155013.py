def Knap(a,b,w):
    # declare an empty dictionary 
    newArr = []
    for i,j in zip(a,b):
        smallArr = []
        smallArr.append(i)
        smallArr.append(j)
        newArr.append(smallArr)
    
    i = 0 
    # at position 0 is the weight and at position 1 is the value 
    # goal is to find highest value but not greater than W 
    value = 0 
    while i < len(newArr)-1:
        if (newArr[i][0] + newArr[i+1][0]) <= w:
            # value = newArr[i][1] + newArr[i+1][1] 
            print('value',value ,'>',newArr[i][1] + newArr[i+1][1])
            if value > newArr[i][1] + newArr[i+1][1]:
                continue
            else:
                value =  newArr[i][1] + newArr[i+1][1] 

        i +=1
    print('v',value)  

        

Knap([5,4,6,3],[10,40,30,50],50)    