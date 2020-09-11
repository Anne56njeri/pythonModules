def word(pattern,str):
    # first I'd check if they are the same length if not return false 
    # loop through both pattern and str
    # both are depedant on whether they are alike or not
    # check one pattern then check the other pattern 
    
    string = str.split(" ")
    
    if len(string) != len(pattern):
        return False 
    print(set(pattern))
    print(set(str))
        
    print(len(pattern),len(string))
print(word("abba","dog cat cat fish"))       
