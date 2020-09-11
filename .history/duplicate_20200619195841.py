def duplicate(str):
    # brute force approach 
    # is storing the substring and checking how many times they
    # occur
    # dictionary key is the substring and occurrences is how many
    # times   its occurred 
    words ={}
    # pointers
    left = 0
    right = 1
    new = []
    while right <= len(str) and left < len(str) -1:
        
        if right == len(str):
            left +=1
        else:    
            right +=1
        words[str[left:right]] = 0

    for i in words:
        words[i] = str.count(i)

    print(words)
    for i in words:

        if words[i] >=2:
            new.append(i)
    print(words)
    answer = new[0]
    j = 0   
    
    while j < len(new)-1:
        if len(answer) < len(new[j+1]):
           answer = new[j+1]
           
        j +=1   
    print(answer)
       
duplicate("aaaaaaaaaaa")