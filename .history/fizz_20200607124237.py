def fizz(num):
    newNumber = []
    for i in range(1,num+1):
        newNumber.append(i)

    for j in range(len(newNumber)): 
        if i % 3== 0:
            newNumber[j] = "Fizz"
        else:
            newNumber[j] = newNumber[i]
    print(newNumber)        
fizz(8)        