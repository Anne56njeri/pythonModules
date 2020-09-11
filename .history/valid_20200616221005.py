# Ipv4 --> 4 decimal numbers,between 0 to 255
# leading zero's is invalid 
# check whethere its a digit between 0 to 255 
import string

def valid(str):
    if str[len(str)-1] == ":" or str[len(str)-1] == ".":
        return "Neither"

    address = str.split(".")
    numbers = range(0,256)
   

    
       
    if len(address) == 4:
        for a in address:
        
            if a.isdigit() == False:
                return "Neither"
            if int(a) not in numbers:
                return "Neither"
            else:
                if len(a) == 2 and a[0] == "0":
                    return "Neither"
                    
        return "IPV4"
                  
                        
    elif len(str.split(" :")):
        newAddress = str.split(":")
        i = 0
        while i < len(newAddress)-1:
            print(newAddress[i])
            well = all(c in string.hexdigits for c in newAddress[i])
            if newAddress[i] == "":
                return "Neither"
            if well == False:
                return "Neither"
            i +=1 
        return "IPV6"          

# "12..33.4"
# "172.16.254.1"
print(valid("256.256.256.256"))