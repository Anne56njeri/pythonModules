def countingValleys(str):
    # no need to split cause you can traverse throught a str
    # how to differentiate between mountain and valley 
    # mountain you go up then down 
    # valley you go down then up 

    valley = 0 
    seaLevel = 0 
    mountain = 0
    journey = 0 
    
    i = 0 
    while i < len(str):
        if str[i] == "U" and seaLevel == 0:
           mountain +=1
           seaLevel +=1
        if  str[i] == "D" and seaLevel > 0: # meaning we are above sea level and we have to come down 
            mountain -=1 
            seaLevel -=1 
        if str[i] == "D" and seaLevel <= 0:
            valley -=1 
            seaLevel -=1 
        if str[i] == "U"         

                 
        
        print("valley --->",valley)
        # print("sea level ---->",seaLevel)
        # print("mountain ------->",mountain)
        i +=1         
    # print(journey)
        
countingValleys("UDDDUDUU")   
# "UDDDUDUU"