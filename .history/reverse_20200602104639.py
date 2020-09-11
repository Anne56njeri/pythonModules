def reversedString(str):
    empty = ""
    start = 0 
    end = len(str) -1 
    while(end >= 0):
        empty += str[end]
        end -=1
    print(empty) 
        
reversedString("ab-ce-fj")    

    
