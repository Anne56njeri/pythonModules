from itertools import permutations

def sequence(n,k):
    newArr = permutations([1,2,3])
    for li in newArr:
        print(type(li))

sequence(3,3)
    