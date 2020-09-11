def Hamming(x,y):
    a = f'{x:04b}'
    b = f'{y:04b}'
    newArr = []
    for i,j in zip(a,b):
        if i !=j:
            newArr.append(i)
            newArr.append(j) 
    total = [int(x) for x in newArr]
    r      
           

   
    
print(Hamming(1,4))    