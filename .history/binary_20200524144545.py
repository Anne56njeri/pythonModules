def solution(N):
    print(N)
    maximumCount = 0
    
    number = format(N,"b")
    print("wow",number)
   
    
    s = [str(i) for i in number] 
    binary = int("".join(s))
    intialNumber = None 
    answer = 0
    totalCount = 0
    print("binary",number)
   

   
    
    for i in range(len(str(number))):
        
        if number[i] == '1':
            if intialNumber is not None and (intialNumber + int(number[i]) == 2) and maximumCount >0:
                print("max",maximumCount)
                return maximumCount
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
               
                answer = maximumCount 
    print("answer",answer)                   
    return 0
                
       

solution(15)                