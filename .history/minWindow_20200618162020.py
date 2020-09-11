# for this question we have two pointers 
# left pointer 
# right pointer 
# we move the right pointer and maintain the position of the left pointer 
# when we find the word we move the left pointer 
# store that word its shortest form 
# we keep moving the right pointer 
# sz,azjskfzts
def minWindow(str1,str2):
    # left = 0 
    # right = 0
    # j = 0
    # words = []
    myChars = set(str1)
    smallest = ""
    current = {}
    
    for i,char in enumerate(str2):
        if char in myChars:
            current[char] = i 
            print(current)
    
    # while left < len(str2) and right < len(str2):
    #     for c in str1:
    #         if c in str2[left:right]:
    #             newWord = str2[left:right]
    #             words.append(newWord)
    #             print(words)
    #             left +=1 
    #         else:
    #             right +=1   
     
          

minWindow("sz","azjskfzts")    
    