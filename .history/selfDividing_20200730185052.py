def dividing(upper,lower):
    newArr = []
    numbers = range(upper,lower+1)
    for i in numbers:
        if i > 0 and i < 10:
            newArr.append(i)
        elif i % 10 != 0:  
            newArr.append()  
dividing(1,22)        