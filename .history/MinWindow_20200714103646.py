# pseducode 
# "ADOBECODEBANC"
# "ABC"
#  if  n(string) is less than k then return false
# have a left and right pointer where both start from the begining and right increases the window size and left reduces the window size 
# make a dictionart for the char in k and the count of unique char in k 


def small(n,k):
    uniqueChar = {}
    nonChar = {}
    uniqueCount = 0
    minCount = 0 
    for i in k:
        if i not in uniqueChar:
            uniqueChar[i] = 1
        else:
            uniqueChar[i] +=1
    for i in n:
        if i not in nonChar:
            nonChar[i] = 1
        else:
            nonChar[i] +=1        
       

    if len(k) > len(n):
        return 'false'

    left = 0 
    right = 1
    

    
    while left < len(n) and right < len(n):
        if n[left:right] in uniqueChar:
            print(n[left:right])
            right +=1

small("ADOBECODEBANC","ABCC")        
