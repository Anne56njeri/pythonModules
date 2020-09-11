def reversedString(str):
    empty = ""
    start = 0 
    end = len(str) -1 
    while(end > 0):
        empty = start[end]
        end -=1
    
