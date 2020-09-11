def solution(N):
    print(N)
    maximumCount = 0
    binaryNumber = []
    well = format(9,"b")
    print("wow",well)
    while( N >= 1):
        N = int(N / 2)
        # print("this",N)
        print("N",N/2,"well",N%2)
        if N % 2 == 0 :
            
            binaryNumber.append(0)
        else:
            binaryNumber.append(1)
    #  then reverse the number 
    number = list(reversed(binaryNumber))
    s = [str(i) for i in number] 
    binary = int("".join(s))
    intialNumber = None 
    lastNumber = None 
    totalCount = 0
    print("binary",str(binary))
    print("number",number)

   
    
    for i in range(len(str(binary))):
       
        if number[i] == 1:
            intialNumber = 1
            
            
        if i < len(number)-1:   
            if number[i] == 0 and number[i+1] :
                lastNumber = 1
                
              
        if intialNumber is not None and lastNumber is not  None  and number[i] == 0:
           
            maximumCount = maximumCount + 1
                         

        else:
            totalCount = maximumCount 
            maximumCount = 0
    # return 0
        

    print("total",totalCount)
                
       

solution(9)                