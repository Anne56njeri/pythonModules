def duplicate(str):
    # brute force approach 
    # is storing the substring and checking how many times they
    # occur
    # dictionary key is the substring and occurrences is how many
    # times   its occurred 
    words ={}
    # pointers
    left = 0
    right = len(str)
    new = []
    while right >= 1 and left < len(str) -1:
        words[str[left:right]] = 0
        left +=1
    print(words)     

    # for i in words:
    #     words[i] = str.count(i)

    # print(words)
    # for i in words:

    #     if words[i] >=2:
    #         new.append(i)
    # print(words)
    # if new == []:
    #     return " "
    # answer = new[0]
    # j = 0  

    
    # while j < len(new)-1:
    #     if len(answer) < len(new[j+1]):
    #        answer = new[j+1]
           
    #     j +=1   
    # print(answer)
       
print(duplicate("banana"))