def fizz(num):
    newNumber = []
    string = " "
    for i in range(1,num+1):
        newNumber.append(i)

    for j in range(len(newNumber)): 
        if newNumber[j] % 3== 0:
            newNumber[j] = "Fizz"
        elif newNumber[j] % 5 == 0:
            newNumber[j] = "Buzz"
        elif newNumber[j] % 3 == 0 and newNumber[j] % 5 == 0:
            newNumber[j] ="StringHeader"      
        else:
            newNumber[j] = newNumber[j]
    
    string = [str]
    print(newNumber)        
fizz(8)        