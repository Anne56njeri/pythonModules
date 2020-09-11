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
            # we check its IPV6
            print("not IPv4")             
    print(address)
valid("172.16.254.02")