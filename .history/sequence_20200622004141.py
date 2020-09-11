from itertools import permutations

# join takes a list of strings so convert them to a list first 

def sequence(n,k):
    newArr = permutations(range(1,n+1))
    finalArr = []
    for i in range(len(newArr)):
        well = ''.join(map(str,newi))
        finalArr.append(well)

    return finalArr[k-1]    
    
            


print(sequence(4,9))
    