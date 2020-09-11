from itertools import permutations

def Time(A):
    # getting the different permutations 
    # get the one that falls between 0000 and 2359 
    # then place the semi colon in the proper place 
    # otherwise return an empty string 
    perm = permutations(A)
    newArray = []
    for i in list(perm):
        string = " ".join
        newArray.append(str(i))
    print(newArray)    
Time([1,2,3,4])        
