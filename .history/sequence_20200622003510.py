from itertools import permutations
import functools
import operator

def sequence(n,k):
    newArr = permutations([1,2,3])
    finalArr = []
    for li in newArr:
        well = ''.join(str(i) for i in li)
            


sequence(3,3)
    