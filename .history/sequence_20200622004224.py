from itertools import permutations

# join takes a list of strings so convert them to a list first 

def sequence(n,k):
    newArr = permutations(range(1,n+1))
    finalArr = []
    for li in newArr:
        well = ''.join(map(str,li))
           
    
            


print(sequence(4,9))
    