from itertools import permutations
import functools
import operator

def sequence(n,k):
    newArr = permutations([1,2,3])
    finalArr = []
    for li in newArr:
        well = functools.reduce(operator.add,str(li))
    

sequence(3,3)
    