def Hamming(x,y):
    a = f'{x:04b}'
    b = f'{y:04b}'
    newArr = []
    for i,j in zip(a,b):
        if i !=j:
            newArr.append(i)
            newArr.append(j)
    return sum(newArr)        

   
    
print(Hamming(1,4)    