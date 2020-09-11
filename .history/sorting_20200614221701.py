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
    result = None
    j = 1
    while j < n-1:
        print(numbers[i],'<',numbers[i+1],"  ",numbers[i])


    

    print(numbers)
wavesort([3, 6, 5, 10, 7, 20])    
