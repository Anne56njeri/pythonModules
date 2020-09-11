def Fizz(n):
    numbers = []
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            numbers.append("F") 
