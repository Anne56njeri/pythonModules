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
    print("binary",str(binary))
   

   
    
    for i in range(len(str(number))):
        print(number[i])
        if number[i] == 1:
            intialNumber = 1
            
            
        if i < len(number)-1:   
            if number[i] == 0 and number[i+1] :
                lastNumber = 1
                
              
        if intialNumber is not None and lastNumber is not  None  and number[i] == 0:
           
            maximumCount = maximumCount + 1
            print("total",totalCount)
                        

        else:
            totalCount = maximumCount 
            maximumCount = 0
  
        

    print("total",totalCount)
                
       

solution(9)                