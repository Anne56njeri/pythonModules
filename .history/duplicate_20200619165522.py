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
    while right <= len(str):
        print(str[left:right])
        if right == len(str):
            left +=1
        else:    
        
        right +=1

duplicate("banana")