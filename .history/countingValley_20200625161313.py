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
        if str[i] == "D" and mountain >1 :
            mountain      
        
 
        print("valley-->",valley)
        # print("mountain --->",mountain)
        i +=1         
    # print(journey)
        
countingValleys("UDDDUDUU")   
# "UDDDUDUU"