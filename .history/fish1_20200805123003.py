def fish(A,B):
    # we place fish moving downwards to a downstream stack 
    # then when its not empty we'll check with the empty at A[i]
    # if it eats that fish we deduct it from the alive fish and del from A 
    # otherwise we shall pop from the down stream stack 
    downStream = []
    j = 0 
    aliveFish = 0
    while j < len(B):
        
        if downStream != []:
            print('down',downStream[-1],'up',A[j])
            if downStream[-1] < A[j]:
                downStream.pop()
        else:
            aliveFish +=1        
         
               
        
          
        j +=1     
    return aliveFish + len(downStream)
    
       
print(fish([4,3,2,1,5],[0,1,0,0,0]))    