# for this question we have two pointers 
# left pointer 
# right pointer 
# we move the right pointer and maintain the position of the left pointer 
# when we find the word we move the left pointer 
# store that word its shortest form 
# we keep moving the right pointer
# how do we get a substring that has all search strings 
# sz,azjskfzts
def minWindow(strArr):
    searchString = strArr[1]
    containsString = strArr[0]
    # left pointer
    left = 0 
    # right pointer
    right = 0 
    realCount = len(searchString)

    while left < len(containsString) and right < len(containsString):
        for c in 



   
     
          

minWindow(["aadadafebaa", "aedd"])    
    