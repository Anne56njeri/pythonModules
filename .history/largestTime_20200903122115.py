from itertools import permutations

def Time(A):
    # getting the different permutations 
    # get the one that falls between 0000 and 2359 
    # then place the semi colon in the proper place 
    # otherwise return an empty string 
    A = [str(i) for i in A]
    perm = permutations(A)


    newArray = []
    arr = []
    for i in list(perm):
        string = "".join(i)
        newArray.append(string)
    newArray = [int(i) for i in newArray]
    for i in newArray:
        if i > 0000 and i =<2359:
            arr.append(i)
    print(arr)        

        
        
Time([1,2,3,4])        
