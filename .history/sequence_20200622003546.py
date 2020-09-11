from itertools import permutations
import functools
import operator
# join takes a list of strings so convert them to a list first 

def sequence(n,k):
    newArr = permutations([1,2,3])
    finalArr = []
    for li in newArr:
        well = ''.join(str(i) for i in li)
        print(well)
            


sequence(3,3)
    