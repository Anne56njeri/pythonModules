def solution(N):
    print(N)
    maximumCount = 0
    
    number = format(N,"b")
    
    intialNumber = None 
    answer = []
   
    for i in range(len(str(number))):
        
        if number[i] == '1':
            if intialNumber is not None and (intialNumber + int(number[i]) == 2) and maximumCount > 0:
                answer.append(maximumCount)
            else:
               
                intialNumber = 1
           
            
            maximumCount = 0 
        if number[i] == '0':
            maximumCount +=1 
    if len(answer) == 0:
        print(0)
        return 0
    else:
        print("answer",max(answer))
        return max(answer)          
    
    

   
                
       

solution(15)                