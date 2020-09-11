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
                  
                        
    elif len(str.split(":")) == 8:
        newAddress = str.split(":")
        i = 0
        while i < len(newAddress)-1:
            print(newAddress[i])
            well = all(c in string.hexdigits for c in newAddress[i])
            if newAddress[i] == "":
                return "Neither"
            if len(newAddress[i]) == 5 and newAddress[i]"0") == 4:
                print("here")
                print(newAddress[i][3])
                return "Neither"
            if well == False:
                return "Neither"
            i +=1 
        return "IPV6"    
    else:
        return "Neither"          

# "12..33.4"
# "172.16.254.1"
print(valid("2001:0db8:85a3:0:0:8A2E:0370:73341"))