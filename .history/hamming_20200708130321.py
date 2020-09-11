def Hamming(x,y):
    # This specifies leading 0, 8 digits, binary.
    a = f'{x:032b}'
    b = f'{y:032b}'
    newArr = []
    for i,j in zip(a,b):
        if i !=j:
            newArr.append(i)
            newArr.append(j) 
    total = [int(x) for x in newArr]
    return sum(total)      
           

   
    
print(Hamming(1,4))    