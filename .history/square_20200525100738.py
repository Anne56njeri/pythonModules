

def square_digits(num):

    square = []
    digits = f"{num}"
    
    for n in digits:
        square.append(int(n)**2)
    s = [str(i) for i in square]
    answer = "".join(s)    
    print(square)
   
square_digits(9119)       