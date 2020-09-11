from itertools import permutations
import functools
import operator

def sequence(n,k):
    newArr = permutations([1,2,3])
    finalArr = []
    for li in newArr:
        well = ''.join(str(li))
        finalArr.append(well)
    print(finalArr)    


sequence(3,3)
    