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
    # if arr[1] is greater than left and right elements then 
    # same pattern will be followed 
    # else the vice versa is true 
    # will be followed by the array elements
    print(numbers[1])
    
    if ( numbers[1] < numbers[0] and numbers[1] < numbers[2]):
        for i in range(i,len(numbers)-1,2):
            print('value',i)
wavesort([1, 5, 3, 7, 2, 8, 6])
