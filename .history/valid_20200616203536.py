# Ipv4 --> 4 decimal numbers,between 0 to 255
# leading zero's is invalid 
# check whethere its a digit between 0 to 255 
def valid(str):
    address = str.split(".")
    numbers = range(0,256)
    for a in address:
        if int(a in numbers:
            print(a)
        else:
            print("false")    
    print(address)
valid("172.16.254.01")