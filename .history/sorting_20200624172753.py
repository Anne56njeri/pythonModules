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
    # if arr[1] is greater than left and right elements then 
    # same pattern will be followed 
    # else the vice versa is true 
    # will be followed by the array elements
    print(numbers)
    if (numbers[1] < numbers[0] and numbers[1] < numbers[2]):
       
        for i in range(1,n-1,2):
            print(numbers[i])

            if numbers[i] <= numbers[i-1] and numbers[i] < numbers[i+1]:
                result = True
            else:
                # for further ahead break from the loop 
                print('heree')
                result = False
                break
        # we check the last element  
        if result == True and n %2 == 0:
            
            if numbers[n-1] >=  numbers[n-2]:
                result = False  
    else:
        return False 

    return result                        

print(wavesort([0, 1, 2, 4, 1, 1, 1]))
# [0, 1, 2, 4, 1, 1, 1]
# [0, 2, 4, 4, 4, 14, 22]
