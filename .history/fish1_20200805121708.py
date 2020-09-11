def fish(A,B):
    # we place fish moving downwards to a downstream stack 
    # then when its not empty we'll check with the empty at A[i]
    # if it eats that fish we deduct it from the alive fish and del from A 
    # otherwise we shall pop from the down stream stack 
    downStream = []
    j = 0 
    aliveFish = 5
    while j < len(B):
        if downStream != []:
            print('down',downStream[-1],'up',A[j])
            if downStream[-1] > A[j]:
               aliveFish -=1
            else:
                aliveFish -=1
                downStream.pop()
        if B[j] == 1:
            downStream.append(A[j]) 
            A.remove(A[j])      
            B.remove()     
        
          
        j +=1     
    return aliveFish + len(downStream)
    
       
print(fish([4,3,2,1,5],[0,1,0,0,0]))    