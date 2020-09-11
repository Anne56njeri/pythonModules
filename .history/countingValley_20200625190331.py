def countingValleys(str):
    # starts from sealevel == 0 
    # valley moves down then up to sea level 
    # How do you identify a valley ?
    # moves down from sea level and up top sea level 
    valleyCounter =  0
    level = 0 
    i = 0 
    while i < len(str):
        if str[i] == 'U':
            level +=1 
        else:
            level -=1 
        i +=1

        print("seaLevel")           


    
        
countingValleys("DDUUDDUDUUUD")   
# "UDDDUDUU"
# "DDUUDDUDUUUD"