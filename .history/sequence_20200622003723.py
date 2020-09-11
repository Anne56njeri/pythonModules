from itertools import permutations
import functools
import operator
# join takes a list of strings so convert them to a list first 

def sequence(n,k):
    newArr = permutations(range(1,))
    finalArr = []
    for li in newArr:
        well = ''.join(map(str,li))
        finalArr.append(well)
    return finalArr[k]    
    
            


sequence(3,3)
    