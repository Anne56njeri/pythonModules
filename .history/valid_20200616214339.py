# Ipv4 --> 4 decimal numbers,between 0 to 255
# leading zero's is invalid 
# check whethere its a digit between 0 to 255 
import string

def valid(str):
    if str[len(str)-1] == ":" or str[len(str)-1] == ".":
        return "Neither"
    address = str.split(".")
    numbers = range(0,256)
    result = None
    for a in address:
       
        if len(address) == 4:
            if a.isdigit():
                
                if int(a) in numbers:
                    if len(a) == 2 and a[0] == "0":
                        result = "Neither"
                        
                    else:
                        result = "IPv4"
                         
            result = "Neither"            

        else:
            newAddress = str.split(":")
            i = 0
            while i < len(newAddress)-1:
                print(newAddress[i])
                well = all(c in string.hexdigits for c in newAddress[i])
                
                if well == True:
                    result = "IPV6"
                else:
                    result = "Neither"
                i +=1 
    return result            


print(valid("172.16.254.1"))