def solution(N):
    print(N)
    maximumCount = 0
    
    number = format(N,"b")
    print("wow",number)
   
    
    s = [str(i) for i in number] 
    binary = int("".join(s))
    intialNumber = None 
    
    totalCount = 0
    print("binary",number)
   

   
    
    for i in range(len(str(number))):
        
        if number[i] == '1':
            if intialNumber is not None and (intialNumber + int(number[i]) == 2) and maximumCount >0:
                
                print("count",totalCount)
            else:
                intialNumber = 1
            totalCount = maximumCount
               
            maximumCount = 0 
        
        if number[i] == '0':

            maximumCount +=1 

        if totalCount > maximumCount:
            print("t",totalCount)
            answer = totalCount
        else:
            print("max",max)
            answer = maximumCount        
    print("answer",answer)
                
       

solution(1041)                