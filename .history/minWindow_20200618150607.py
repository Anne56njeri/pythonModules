# for this question we have two pointers 
# left pointer 
# right pointer 
# we move the right pointer and maintain the position of the left pointer 
# when we find the word we move the left pointer 
# store that word its shortest form 
# we keep moving the right pointer 
# sz,azjskfzts
def minWindow(str1,str2):
    left = 0 
    right = 0
    word = list(str1)
    print(word)
    
    while left < len(str2) and right < len(str2):
        # print(str2[left:right])
        if str2[left:right] in word:
            newWord = str2[left:right]
            print(newWord)
            left +=1
        else:
            right +=1


        
        

    

minWindow("sz","azjskfzts")    
    