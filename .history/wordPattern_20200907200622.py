def word(pattern,str):
    # first I'd check if they are the same length if not return false 
    # loop through both pattern and str
    # both are depedant on whether they are alike or not
    # check one pattern then check the other pattern 
    
    string = str.split(" ")
    note = {}
    if len(string) != len(pattern):
        return False 
    if len(set(pattern)) != len(set(string)):
        return False 
    for i in range(len(pattern)):
        if pattern[i] in note:
            if note[pattern[i]] != string[i]:
                return False
        else: 
            if       
              


                 
         
    
print(word("aba","dog cat cat"))       
