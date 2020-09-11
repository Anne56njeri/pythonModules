def jumpingClouds(c):
    i = 0 
    jumps = 0 
    while i < len(c):
        if c[i+2] == 0:
            jumps +=1
        elif c[i+1] == 0:
            jumps +=1    


jumpingClouds([0,0,1,0,0,1,0])    