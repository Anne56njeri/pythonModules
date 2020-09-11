# pseducode 
# "ADOBECODEBANC"
# "ABC"
# have a left and right pointer where both start from the begining and right increases the window size and left reduces the window size 
# make a dictionart for the char in k and the count of unique char in k 


def small(n,k):
    uniqueChar = {}
    uniqueCount = 0
    for i in k:
        if i not in uniqueChar:
            uniqueChar[i] = 1
        else:
            uniqueChar[i] +=1
    for i in uniqueChar:
        if uniqueChar[i] > 1:
            uniqueCount += uniqueChar[i]     
            


    #  if  n(string) is less than k then return false
    if len(k) > len(n):
        return 'false'

    left = 0 
    right = 0 
    print(uniqueChar)
    # while left < len(n) and right < len(n):

small("ADOBECODEBANC","ABCC")        
