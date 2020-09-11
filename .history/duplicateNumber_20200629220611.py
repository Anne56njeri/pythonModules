def duplicate(arr):
    numbers = set()
    i = 0 
    while i < len(arr):
        if arr[i]in numbers:
            print('well',arr[i])   
        else:
            numbers.add(arr[i])   
            del arr[i] 
            
        print(numbers)    
          

duplicate([1,3,4,2,2])    