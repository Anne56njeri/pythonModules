def fish(A,B):
    # we place fish moving downwards to a downstream stack 
    # 
    
    downStream = []
    j = 0 
    aliveFish = 0
    
    for j in range(len(B)):
        print('alive',aliveFish)
        if B[j] == 0:
            while downStream !=[] and downStream[-1] < A[j]:
                downStream.pop()
            if downStream == []:
                aliveFish +=1   
        else:
            downStream.append(A[j])         
    return aliveFish + len(downStream)
# print(fish([4,3],[1,1]))    
print(fish([4,3,2,1,5],[0,1,0,0,0]))    