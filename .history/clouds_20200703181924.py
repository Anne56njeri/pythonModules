def jumpingClouds(c):
    i = 0 
    jumps = 0 
    while i < len(c)-2:
        if c[i] == 0 and c[i+2] == 0:
            print('here')
            print('c---->',c[i],'i-->',i)
            jumps +=1
            # i +=2
        elif c[i] == 0 and c[i+1] == 0:
            print('here2')
            print('c---->',c[i],'i-->',i)
            jumps +=1    
        i +=1 
    print(jumps)            


jumpingClouds([0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0 1 0 1 0 0 0 1 0 0 1 0 0 0 1 0 1 0 0 0 0 0 0 0 0 1 0 0 1 0 1 0 0])    