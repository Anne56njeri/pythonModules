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
    if arr[i] > arr[0] and arr[1] > arr[2]:
        for i in range(i,n-1,2):
            print('value',i)
wavesort([0, 1, 2, 4, 1, 1, 1])
