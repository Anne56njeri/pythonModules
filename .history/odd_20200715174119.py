def odd(A):
    # return the value that doesn't have a pair 
    # a dictionary to keep track of the number of times 
    # an element has been repeated 
    newDict = {}
    for i in A:
        if i in newDict:
            newDict[i] +=1
        else:
            newDict[i] = 1
        if newDict[i] == 1:
            return i    


print(odd([9,3,9,3,9,7,9]))  