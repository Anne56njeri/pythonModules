

def square_digits(num):

    square = []
    digits = "num"
    s = [str(i) for i in num]
    for i in range(len(num)):
        square.append(num[i]**num[i])
    print(square) 
square_digits(9119)       