def wavesort(arr):
    # sort the numbers first 
    numbers = sorted(arr)
    # swap the numbers 
    n = len(numbers)
    i = 0 
    while i < n-1:
        temp = numbers[i]
        i+=1

    print(numbers)
wavesort([20, 10, 8, 6, 4, 2])    
