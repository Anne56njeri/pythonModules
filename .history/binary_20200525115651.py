def solution(N):
    print(N)
    maximumCount = 0
    
    number = format(N,"b")
    print("wow",number)
   
    
    # s = [str(i) for i in number] 
    # binary = int("".join(s))
    intialNumber = None 
    answer = []
    
    print("binary",number)
   

   
    
    for i in range(len(str(number))):
        
        if number[i] == '1':
            if intialNumber is not None and (intialNumber + int(number[i]) == 2) and len(answer) > 1:
                answer.append(maximumCount)
                print("")
               
                 
            else:
                print("max",answer)
                intialNumber = 1
           
            
            maximumCount = 0 
        if number[i] == '0':
            maximumCount +=1 
        # return max(answer)      
    
    return 0

   
                
       

solution(15)                