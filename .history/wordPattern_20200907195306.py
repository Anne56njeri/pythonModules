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
    note[pattern[0]] = [string[0]]
    for i in range(1,len(string)):
        if string[i] in
         
    
print(word("aba","dog cat cat"))       
