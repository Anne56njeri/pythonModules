def countingValleys(str):
    # no need to split cause you can traverse throught a str
    valley = 0 
    seaLevel = 0 
    journey = 0 
    i = 0 
    while i < len(str):
        
        if str[i] == 'U':
            journey +=1 
        if str[i] == 'D':
            journey -=1
        print('journey',journey)    
        if journey == seaLevel:
            valley +=1     
                
        i+=1 
    print(valley-1)
countingValleys("DDUUUUDD")   
# "UDDDUDUU"