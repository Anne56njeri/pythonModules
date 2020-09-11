def duplicate(arr):
    numbers = set()
    i = 0 
    while i < len(arr):
        if arr[i] not in numbers:
            numbers.add(arr[i])  
            del arr[i]
        else:
            print(arr[i])   
        i +=1    
    print(arr)  
    print(numbers)       

duplicate([1,3,4,2,2])    