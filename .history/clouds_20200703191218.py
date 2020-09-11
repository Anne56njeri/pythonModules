def jumpingClouds(c):
    i = 0 
    jumps = 0 
    lastCloud = len(c)-1

    while i < lastCloud:
                   
        # if  i+1 == lastCloud:
        #     jumps +=1
        #     i +=1
        #     print('here')
        #     print('c---->',c[i],'i-->',i,'jumps',jumps)
        if i != lastCloud:
            if c[i+2] == 0:    
                jumps +=1
                i =i+2
                print('c---->',c[i],'i-->',i,'jumps',jumps)
        elif  c[i+1] == 0:
            print('here2')
            
            jumps +=1  
            
            i +=1 
            print('c---->',c[i],'i-->',i,'jumps',jumps)
    print(jumps)            


jumpingClouds([0, 0, 0, 1, 0, 0])    