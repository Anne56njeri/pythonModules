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
        if str[i] == "U":
            mountain +=1 
            valley +=1
        if str[i] == "D":
            mountain -=1
            valley -=1 
        if valley == seaLevel:
            journey +=1    
        
        i +=1         

        
countingValleys("DDUUUUDD")   
# "UDDDUDUU"