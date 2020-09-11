def solution(N):
    print(N)
    maximumCount = 0
    
    number = format(9,"b")
    print("wow",number)
   
    
    s = [str(i) for i in number] 
    binary = int("".join(s))
    intialNumber = None 
    lastNumber = None 
    totalCount = 0
    print("binary",number)
   

   
    
    for i in range(len(str(number))):
        
        if number[i] == '1':
            if intialNumber is not None and (intialNumber + int(number[i]) == 2) and maximumCount >0:
                print("count",maximumCount)
            else:
                intialNumber = 1
            maximumCount = 0 
        if number[i] == '0':
            maximumCount +=1 
            totalCount = maximumCount

        
    
        

    print("total",totalCount)
                
       

solution(9)                