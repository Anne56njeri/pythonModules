def countingValleys(str):
    # starts from sealevel == 0 
    # valley moves down then up to sea level 
    # How do you identify a valley ?
    # moves down from sea level and up top sea level 
    level = 0
    valley = 0 



    i = 0 
    while i < len(str):
        if str[i] == 'U':
            level +=1
            if level == -1:
                valley +=1 
        else:
            level =-1        

        i +=1


    
        
countingValleys("DDUUDDUDUUUD")   
# "UDDDUDUU"