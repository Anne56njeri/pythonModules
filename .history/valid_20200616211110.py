# Ipv4 --> 4 decimal numbers,between 0 to 255
# leading zero's is invalid 
# check whethere its a digit between 0 to 255 
import string

def valid(str):
    
    address = str.split(".")
    numbers = range(0,256)
    for a in address:
        if len(address) == 4:

            if int(a) in numbers:
                if len(a) == 2 and a[0] == "0":
                    return "Neither"
            else:
                    return "IPv4"
        else:
            newAddress = str.split(":")
            i = 0
            while i < len(newAddress)-1:
                # print(type(newAddress[i]))
                well = all(c in string.hexdigits for c in newAddress[i])
                if well == True:
                    return "IPv6"
                else:
                    return "Neither"
                i +=1  

valid("172.16.254.1")