# Ipv4 --> 4 decimal numbers,between 0 to 255
# leading zero's is invalid 
# check whethere its a digit between 0 to 255 
def valid(str):
    
    address = str.split(".")
    numbers = range(0,256)
    for a in address:
        if len(address) == 4:

            if int(a) in numbers:
                if len(a) == 2 and a[0] == "0":
                    return False
            else:
                    return True
        else:
            newAddress = str.split(":")
            i = 0
            while i < len(newAddress)-1:
                print(newAddress[i])
                if int(newAddress[i] )

valid("2001:0db8:85a3:0:0:8A2E:0370:7334")