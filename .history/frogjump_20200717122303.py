# use the brute force approach then optimize 
# and test edge cases 
# o(n)

def jump(X,Y,D):
    if X == Y:
        return 0
    if D < 1:
        return 0
    else:
        count = 0
        while X <= Y:
            X = X+D 
            count +=1 
        print('',count)           



jump(10,85,30)