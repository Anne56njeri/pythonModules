# use the brute force approach then optimize 
# and test edge cases 
# o(n)
import math 

def jump(X,Y,D):
    if X == Y:
        return 0
    if D < 1:
        return 0
    else:
        answer  = math.ceil((Y-X) / D)
        print(answer)
        # count = 0
        # while X < Y:
        #     print('hmm')
        #     X = X+D 
        #     count +=1 
        # return count           



print(jump(20,85,30))