def countingValleys(str):
    # no need to split cause you can traverse throught a str
    # how to differentiate between mountain and valley 
    # mountain you go up then down 
    # valley you go down then up 

    valley = 0 
    seaLevel = 0 

    journey = 0 
    mountain = 0 
    i = 0 
    while i < len(str):
        if str[i] == "U" and valley > 0:
            
            valley +=1
        if str[i] == "D" :
            valley -=1 
        if valley == seaLevel:
            journey +=1    
        print("valley-->",valley)
        i +=1         
    print(journey)
        
countingValleys("UDDDUDUU")   
# "UDDDUDUU"