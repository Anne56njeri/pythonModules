def reverse(s):
    # loop through the str 
    # have an empty str 
    word = ""
    newStr = s.split(" ")
    newWord = []

    for i in range(len(newStr)):
        newWord.append(newStr[i][::-1]))
    return " ".join(newWord)    
       
   
print(reverse("Let's take LeetCode contest"))       


    