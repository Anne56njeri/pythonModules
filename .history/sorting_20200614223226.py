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
    result = None
    j = 1
    while j < n-1:
        if  not numbers[j] < numbers[j-1] or  not numbers[j] < numbers[j+1]:
            return "false"
          
        j +=2

        
    return "true"
wavesort([0, 1, 2, 4, 1, 1, 1])    
