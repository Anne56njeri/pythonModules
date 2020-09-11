def duplicate(str):
    # brute force approach 
    # is storing the substring and checking how many times they
    # occur
    # dictionary key is the substring and occurrences is how many
    # times   its occurred 
    words ={}
    # pointers
    left = 0
    right = 0
    while right <= len(str) and left <len(str):
        if right == len(str):
            left +=1
        else:    
            right +=1
        words[str[left:right]] = 0 

    while right <= len(str) and left <len(str):
        if right == len(str):
            if 
            
            left +=1
        else:    
            right +=1
         


duplicate("banana")