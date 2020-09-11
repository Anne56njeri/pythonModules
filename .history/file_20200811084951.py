# a,b --> 2*3 == 2 + 2 + 2 = 6 
# use for loop or a while loop 
def product(a,b):
    if a == 0 or b == 0:
        return 0

    total = 0 
    while b > 0:
        total +=a 
        b -=1 
    print(total)
print(product(2,0))        