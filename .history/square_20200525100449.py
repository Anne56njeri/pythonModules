

def square_digits(num):

    square = []
    digits = f"{num}"
    # s = [str(i) for i in num]
    for n in digits:
        square.append(int(n)**2)
    print(square)
    print(digits) 
square_digits(9119)       