def fizz(num):
    newNumber = []
    for i in range(1,num+1):
        
        if i % 3== 0:
            newNumber[i] = "Fizz"
        else:
            newNumber[i] = newNumber[i]
    print(newNumber)        
fizz(8)        