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
    while right < len(str) and left < len(str):
        print(str[left:right],right)
        if right == len(str)-1:
            left +=1
        else:    
            right +=1
        # print(str[left:right])    
        words[str[left:right]] = 0

    # for i in words:
    #     print(i,"--->",str.count(i))
        
    print(words)              
         


duplicate("banana")