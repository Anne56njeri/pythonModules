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
    while right <= len(str) and left < len(str) -2:
        
        if right == len(str):
            left +=1
        else:    
            right +=1
        words[str[left:right]] = 0

    for i in words:
        words[i] = str.count(i)

    i = 0 
    for i in words:
        if words[i] >=2:
            new.append(i)
           
    for j in range(len(new)-1):
        answer = new[]
        if len(new[j]) > len(new[j+1]) and len(new[j]):
            answer = new[j] 
        else:
            answer = new[j+1] 
            
             



            
        
                 
         


duplicate("geeksforgeeks")