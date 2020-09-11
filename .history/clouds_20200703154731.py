def jumpingClouds(c):
    i = 0 
    jumps = 0 
    while i < len(c)-2:
        if c[i+2] == 0:
            print('here1')
            jumps +=1
        elif c[i+1] == 0:
            print
            print('here')
            jumps +=1 
        i +=1 
    print(jumps)            


jumpingClouds([0,0,1,0,0,1,0])    