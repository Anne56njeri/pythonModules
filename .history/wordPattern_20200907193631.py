def word(pattern,str):
    # first I'd check if they are the same length if not return false 
    # loop through both pattern and str
    # both are depedant on whether they are alike or not
    # check one pattern then check the other pattern 
    
    string = str.split(" ")
    
    if len(string) != len(pattern):
        return False 
    i = 0 
    j = 0 
    Value = ""
    Value2 = ""
    while i < len(pattern)-1 and j < len(string)-1:
        if pattern[i] == pattern[i+1]:
            
               

        i +=1 
        j +=1     
    return True      
    print(len(pattern),len(string))
print(word("abba","dog cat cat dog"))       
