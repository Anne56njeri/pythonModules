def wavesort(arr):
    # sort the numbers first 
    numbers = sorted(arr)
    # swap the numbers 
    n = len(numbers)
    i = 0 
    print(numbers)
    # while i < n-1:
    #     temp = numbers[i]
    #     numbers[i] = numbers[i+1]
    #     numbers[i+1] = temp
    #     i+=2
    for i in range(0,n-1,2):
        numbers[i],numbers[i+1] = numbers[i+1],

    print(numbers)
wavesort([3, 6, 5, 10, 7, 20])    
