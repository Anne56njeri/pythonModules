def fish(A,B):
    # we place fish moving downwards to a downstream stack 
    # then when its not empty we'll check with the empty at A[i]
    # if it eats that fish we deduct it from the alive fish and del from A 
    # otherwise we shall pop from the down stream stack 
    downStream = []
    j = 0 
    aliveFish = len(A)
    fishRemoved = 0
    for j in range(len(B)):
        if B[j] == 0:
            while downStream !=[] and downStream[-1] < A[j]:
                downStream.pop()
            if downStream == []:
                aliveFish +=1    

print(fish([4,3],[0,1]))    
# print(fish([4,3,2,1,5],[0,1,0,0,0]))    