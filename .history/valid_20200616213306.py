# Ipv4 --> 4 decimal numbers,between 0 to 255
# leading zero's is invalid 
# check whethere its a digit between 0 to 255 
import string

def valid(str):
    
    address = str.split(".")
    numbers = range(0,256)
    if str[len(str)-1] == ":" or :
                return "Neither"
    for a in address:
        if len(address) == 4:
            if a.isdigit():
                if int(a) in numbers:
                    if len(a) == 2 and a[0] == "0":

                        return "Neither"
                    else:
                        return "IPv4" 
            return "Neither"            

        else:
            
            else:    
                newAddress = str.split(":")
                i = 0
                while i < len(newAddress)-1:
                    print(newAddress[i])
                    well = all(c in string.hexdigits for c in newAddress[i])
                    
                    if well == True:
                        print("well",well)
                        # return "IPv6"
                    else:
                        return "Neither"
                    i +=1 


print(valid("1.1.1.1."))