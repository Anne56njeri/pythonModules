# for this question we have two pointers 
# left pointer 
# right pointer 
# we move the right pointer and maintain the position of the left pointer 
# when we find the word we move the left pointer 
# store that word its shortest form 
# we keep moving the right pointer
# how do we get a substring that has all search strings 
# we len search string 
# we count the letters in containing strings it should be equal to == len(searchString)

def minWindow(strArr):
    searchString = strArr[1]
    containsString = strArr[0]
    # left pointer
    left = 0 
    # right pointer
    right = 1
    realCount = len(searchString)
    print("realCount",realCount)
    word = ""
    newWord = []

    while left < len(containsString) and right < len(containsString):
        for c in searchString:
            # print(containsString[left:right].count(c))
            # print(containsString[left:right])
            if containsString[left:right].count(c) == realCount:
                
                left +=1 
                word +=containsString[left:right]
            else:
                right +=1    
    newWord = list(word)
    #    




   
     
          

minWindow(["aadadafebaa", "aedd"])    
    