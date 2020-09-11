def fish(A,B):
    # we place fish moving downwards to a downstream stack 
    # Compare the upstream fish with the downStream in fron of it 
    # and remove from the stack all fish less than out one upstream fish 
    #  if we have no downStream 
    #  just count our fish and keep moving
    '''
    Put all downstream swimming fishes on a stack. 
    Any upstream swimming fish has to fight(eat) all fishes on the stack. 
    If there is no fish on the stack, the fish survives. 
    If the stack has some downstream fishes at the end, they also survive.
    '''
    
    downStream = []
    j = 0 
    aliveFish = 0
    
    for j in range(len(B)):
        print('alive',aliveFish)
        if B[j] == 0:
            while downStream !=[]:
                if 
                downStream.pop()
            if downStream == []:
                aliveFish +=1   
        else:
            downStream.append(A[j])         
    return aliveFish + len(downStream)
# print(fish([4,3],[1,1]))    
print(fish([4,3,2,1,5],[0,1,0,0,0]))    