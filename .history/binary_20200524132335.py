def solution(N):
    print(N)
    maximumCount = 0
    binaryNumber = []
    while( N > 0):
        N = int(N / 2)
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
    print("binary",binary)
   
    
    for i in range(len(number)):
        # print("number",number[i])
        if number[i] == 1:
            intialNumber = 1
            
        if i < len(number)-1:   
            if number[i] == 0 and number[i+1] :
                lastNumber = 1
            if intialNumber is not None and lastNumber is not None  and number[i] == 0:
                maximumCount += 1

                
            else:
                totalCount = maximumCount
                maximumCount = 0
        if totalCount > maximumCount:
            print("maximum",totalCount)
        else:
            print             
                
    return 0 

solution(1041)                