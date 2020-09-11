def wavesort(arr):
    # sort the numbers first 
    numbers = sorted(arr)
    # swap the numbers 
    n = len(numbers)
    i = 0 
    result = True
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
    
    if (numbers[1] < numbers[0] and numbers[1] < numbers[2]):
       
        for i in range(1,n-1,2):

            if numbers[i] > numbers[i-1] and numbers[i] > numbers[i+1]:
                result = True
            else:
                result = False
                break
        if result == True and n %2 == 0:
            if numbers[n-1] <= numbers[n-2]:
                result = False  
    else                    

print(wavesort([1, 5, 3, 7, 2, 8, 6]))
