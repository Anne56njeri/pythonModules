from itertools import permutations

def Time(A):
    # getting the different permutations 
    # get the one that falls between 0000 and 2359 
    # then place the semi colon in the proper place 
    # otherwise return an empty string 
    perm = permutations(A)
    
    for i in list(perm):
        print (i)
Time([1,2,3,4])        
