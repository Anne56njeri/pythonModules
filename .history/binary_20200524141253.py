def solution(N):
    print(N)
    maximumCount = 0
    number = format(9,"b")
    s = [str(i) for i in number] 
    binary = int("".join(s))
    intialNumber = None 
    lastNumber = None 
    totalCount = 0
  
   

   
    
    for i in range(len(str(number))):
        print(number[i])
        if number[i] == 1:
           if intialNumber is not None and (int(intialNumber) + number[i] == 2) and maximumCount >0:
                print("max",maximumCount)
           else:
              intialNumber = 1
        if number[i] == 0:
            maximumCount = maximumCount + 1

  
        

    print("total",maximumCount)
                
       

solution(9)                