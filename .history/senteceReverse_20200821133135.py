def reverse(s):
    # loop through the str 
    # have an empty str 
    word = ""
    newStr = s.split(" ")
    newWord = []

    for i in range(len(newStr)):
        newWord[i] = newStr[i][::-1]
    print(newWord)
reverse()        


    