from itertools import permutations

def sequence(n,k):
    newArr = permutations([1,2,3])
    finalArr = []
    for li in newArr:
        well = str(li)
        print(''.join(well))

sequence(3,3)
    