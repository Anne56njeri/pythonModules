def wavesort(arr):
    # sort the numbers first 
    numbers = sorted(arr)
    # swap the numbers 
    n = len(numbers)
    i = 0 
    print(numbers)
    while i < n-1:
        temp = numbers[i]
        numbers[i] = numbers[i+1]
        numbers[i+1] = temp
        i+=2
    #check if number at position i is smaller than its adjacent elements 
    print(numbers)
    result = []
    j = 1
    while j < n-1:
        print(numbers[j],'<',numbers[j-1],' ',numbers[j],'<',numbers[j+1])
        if  numbers[j] < numbers[j-1] and   numbers[j] < numbers[j+1]:
            result.append("true")
        else:
            result.append("false")    
          
        j +=2

        
    print(result)
print(wavesort([0, 4, 22, 4, 14, 4, 2]))   
